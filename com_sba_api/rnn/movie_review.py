import os
from com_sba_api.utils.file_helper import FileReader
from com_sba_api.utils.checker import is_number
from pandas import read_table
import numpy as np
from collections import defaultdict
import math

class MovieReview:
    def __init__(self):
        self.reader = FileReader()

    def hook(self):
        print('==== Hook ====')
        self.load_corpus()

    def load_corpus(self):
        reader = self.reader
        corpus = read_table('./data/movie_review.csv', sep=',', encoding='UTF-8')
        print(f'Corpus Spec : {corpus}')
        return np.array(corpus)

    def count_words(self, traing_set):
        counts = defaultdict(lambda: [0,0])
        for doc, point in traing_set:
            # 영화리뷰가 text 일때만 카운팅
            if is_number(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts

    def word_probabilities(self, counts, total_class0, total_class1, k):
        # 단어의 빈도수를 [단어,p(w|긍정), p(w|부정) ] 형태로 전환
        return [(W, 
                (class0 + k) / (total_class0 + 2 * k),
                (class1 + k) / (total_class1 + 2 * k)) 
                for W, (class0, class1) in counts.items()]

    def class0_probability(self, word_probs, doc):
        # 별도의 토크나이즈 하지 않고 띄어쓰기 만
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        # 모든 단어에 반복
        for word, prob_if_class0, prob_if_class1 in word_probs:
            # 만약 리뷰에 word 가 나타나면 해당 단어가 나올 log 에 확률을 더해줌
            if word in docwords:
                log_prob_if_class0 += math.log(prob_if_class0)
                log_prob_if_class1 += math.log(prob_if_class1)
            # 만약 리뷰에 word 가 없으면 해당 단어가 안나올 log 에 확률을 더해줌
            # 나오지 않을 확률은 log ( 1 - 나올 확률) 로 계산
            else:
                log_prob_if_class0 += math.log(1.0 - prob_if_class0)
                log_prob_if_class1 += math.log(1.0 - prob_if_class1)

        # prob_if_class0 = 


mr = MovieReview()
mr.hook()

        

    

    