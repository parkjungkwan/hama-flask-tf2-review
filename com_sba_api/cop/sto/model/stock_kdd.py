from typing import List
from flask import request
from flask_restful import Resource, reqparse
from flask import jsonify
from com_sba_api.ext.db import db, openSession
from com_sba_api.util.file import FileReader
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.tree import DecisionTreeClassifier # dtree
from sklearn.ensemble import RandomForestClassifier # rforest
from sklearn.naive_bayes import GaussianNB # nb
from sklearn.neighbors import KNeighborsClassifier # knn
from sklearn.svm import SVC # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold  # k value is understood as count
from sklearn.model_selection import cross_val_score
from sqlalchemy import func
from pathlib import Path
from sqlalchemy import and_, or_
from datetime import datetime
from pandas._libs.tslibs.offsets import relativedelta
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from dataclasses import dataclass
from konlpy.tag import Okt
from nltk import word_tokenize, re, FreqDist

import FinanceDataReader as fdr # pip install -U 
import pandas as pd
import json
import numpy as np
import pandas_datareader as pdr
import json
import os
import csv
import requests
import re
import collections
import csv
import json
import pandas as pd


'''
 * @ Module Name : stock.py
 * @ Description : Recommendation for share price transactions
 * @ since 2009.03.03
 * @ version 1.0
 * @ Modification Information
 * @ author 주식거래 AI 추천서비스 개발팀 박정관
 * @ special reference libraries
 *     finance_datareader, konlpy
 * @ 수정일         수정자                   수정내용
 *  -------    --------    ---------------------------
 *  2020.08.01    최윤정          최초 생성
 *  2020.10.29    박정관          모듈 통합 및 개선

''' 

# ==============================================================
# =========================                =====================
# =========================  Data Mining   =====================
# =========================                =====================
# ==============================================================

class StockDm:
    
    def candle_crawling(self, symbol):
        symbol = symbol
        symbol_with_ks = symbol + '.KS'

        end_date = datetime.now()
        start_date = datetime.now()-relativedelta(months=3)
        temp = pdr.get_data_yahoo(symbol_with_ks, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        temp.drop(['Volume', 'Adj Close'], axis=1, inplace=True)

        date_index = temp.index.get_level_values('Date').tolist()

        result = []
        for i in range(len(date_index)):
            result.append({'x': str(date_index[i].strftime('%Y-%m-%d')),
                           'y': list(np.array(temp.iloc[i]).tolist())})
        return result

    # ThreeDays:
    # 통합 워드클라우드를 만들게 될지도 몰라 준비하는 크롤링
    # 3일간의 이슈 검색어를 팔로업한다

    def date(self):
        date = []
        today = datetime.today()
        dt_index = pd.date_range(today, periods=2, freq='-1d')
        dt_list = dt_index.strftime("%Y%m%d").tolist()
        for i in dt_list:
            date.append(i)
        return date

    def news_crawling_1(self, page_number):
        result = []
        date = self.date()
        for regDate in date:
            for i in range(page_number):
                url = "https://finance.naver.com/news/news_list.nhn?mode=LSS3D&section_id=101&section_id2=258&section_id3=402" \
                      "&date={date}&page={page}".format(date=regDate, page=i)
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                a = soup.find_all('dd', {'class': 'articleSubject'})
                for item in a:
                    link = str('https://finance.naver.com{}') \
                        .format(item.find('a')['href']
                                .replace("§", "&sect"))
                    content = self.get_text(link)
                    news = {content: "content"}
                    result.append(news)
        self.get_csv(result)
        return result

    def get_csv(self, result):
        file = open('../static/data/news_threeDays_crawling.csv', 'w', encoding='utf-8', newline='')
        csvfile = csv.writer(file)
        for row in result:
            csvfile.writerow(row)
        file.close()

    def get_text(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        content = ''
        for item in soup.find_all('div', {'id': 'content'}):
            for text in item.find_all(text=True):
                if re.search('▶', text) is not None:
                    break
                content = content + text + "\n\n"
        return content


if __name__ == '__main__':
    stockDf = StockDm()
    crawl = stockDf.news_crawling_1(page_number=100)
    



    # 썸네일 포함한 뉴스 5일치 크롤링
    # csv 파일로 생성하여 DB에 저장한다
    # NewsListCrawler:


    def date(self):
            date = []
            selected = '2020-08-25'
            dt_index = pd.date_range(selected, periods=8, freq='-1d')
            dt_list = dt_index.strftime("%Y%m%d").tolist()
            for i in dt_list:
                print(i)
                date.append(i)
            return date

    def news_crawling_2(self, page_number):
        result = []
        date = self.date()
        for regDate in date:
            for i in range(page_number):
                url = "https://finance.naver.com/news/news_list.nhn?mode=LSS3D&section_id=101&section_id2=258&section_id3=402" \
                      "&date={date}&page={page}".format(date=regDate, page=i)
                html = requests.get(url).text
                soup = BeautifulSoup(html, 'html.parser')
                a = soup.find_all('dd', {'class': 'articleSubject'})
                for item in a:
                    title = item.find('a')['title']
                    link = str('https://finance.naver.com{}') \
                        .format(item.find('a')['href']
                                .replace("§", "&sect"))
                    wdate = self.get_wdate(link)
                    content = self.get_text(link)
                    thumbnail = self.get_thumbnail(link)
                    news = {wdate: "wdate", title: "title", content: "content", link: "link", thumbnail: "thumbnail"}
                    result.append(news)
        self.get_csv(result)
        return result

    def get_csv(self, result):
        file = open('../static/data/final_news_crawling.csv', 'w', encoding='utf-8', newline='')
        csvfile = csv.writer(file)
        for row in result:
            csvfile.writerow(row)
        file.close()

    def get_wdate(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        written_date = soup.find_all(class_='article_sponsor')
        for date in written_date:
            wdate = date.find('span').text
            return wdate

    def get_thumbnail(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        article_image = soup.find_all(class_='end_photo_org')
        for item in article_image:
            src = item.find('img')['src']
            return src

    def get_text(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        content = ''
        for item in soup.find_all('div', {'id': 'content'}):
            for text in item.find_all(text=True):
                if re.search('▶', text) is not None:
                    break
                content = content + text + "\n\n"
        return content


if __name__ == '__main__':
    stockDm = StockDm()
    crawl = stockDm.news_crawling_2(page_number=100)



# Text_mining_create_csv.py 

@dataclass
class Entity:
    context: str = ''
    fname: str = ''
    target: str = ''
    date: str = ''

class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.noun_tokens = []
        self.okt = Okt()
        self.stopword = []
        self.freqtxt = []
        self.date = []

    def tokenize(self):
        filename = r'../static/data/news_threeDays_crawling.csv'
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        texts = self.texts.replace('\n', '')
        tokenizer = re.compile(r'[^ㄱ-힣]')
        self.texts = tokenizer.sub(' ', texts)
        self.tokens = word_tokenize(self.texts)
        _arr = []
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            _ = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len("".join(_)) > 1:
                _arr.append("".join(_))
        self.noun_tokens = " ".join(_arr)

        filename = r'../static/data/stopwords.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            self.stopword = f.read()
        print(type(self.stopword))
        self.noun_tokens = word_tokenize(self.noun_tokens)
        self.noun_tokens = [text for text in self.noun_tokens
                            if text not in self.stopword]
        keyword_list = self.noun_tokens
        self.freqtxt = pd.Series(dict(FreqDist(keyword_list))).sort_values(ascending=False)
        c2 = collections.Counter(keyword_list)
        a = c2.most_common(50)
        file = open('../static/data/news_threeDays_mining.csv', 'w', encoding='utf-8', newline='')
        print(file.name)
        csvfile = csv.writer(file)
        for row in a:
            csvfile.writerow(row)
        file.close()
        return file

if __name__ == '__main__':
    service = Service()
    result = service.tokenize()
    print(result)
