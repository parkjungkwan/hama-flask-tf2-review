from typing import List
from flask import request
from flask_restful import Resource, reqparse
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
from com_sba_api.util.file import FileReader
from flask import jsonify
from com_sba_api.ext.db import db, openSession
import pandas as pd
import json
import os
import pandas as pd
import numpy as np

class UserDto(db.Model):

    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    user_id: str = db.Column(db.String(10), primary_key = True, index = True)
    password: str = db.Column(db.String(1))
    name: str = db.Column(db.String(100))
    pclass: int = db.Column(db.Integer)
    gender: int = db.Column(db.Integer)
    age_group: int = db.Column(db.Integer)
    embarked: int = db.Column(db.Integer)
    rank: int = db.Column(db.Integer)

    # orders = db.relationship('OrderDto', back_populates='user', lazy='dynamic')
    # prices = db.relationship('PriceDto', back_populates='user', lazy='dynamic')
    articles = db.relationship('ArticleDto', back_populates='user', lazy='dynamic')

    def __init__(self, user_id, password, name, pclass, gender, age_group, embarked, rank):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.pclass = pclass
        self.gender = gender
        self.age_group = age_group
        self.embarked = embarked
        self.rank = rank

    def __repr__(self):
        return f'User(user_id={self.user_id},\
            password={self.password},name={self.name}, pclass={self.pclass}, gender={self.gender}, \
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank})'

    
    def __str__(self):
        return f'User(user_id={self.user_id},\
            password={self.password},name={self.name}, pclass={self.pclass}, gender={self.gender}, \
                age_group={self.age_group}, embarked={self.embarked}, rank={self.rank})'


    
    def json(self):
        return {
            'userId' : self.user_id,
            'password' : self.password,
            'name' : self.name,
            'pclass' : self.pclass,
            'gender' : self.gender,
            'ageGroup' : self.age_group,
            'embarked' : self.embarked,
            'rank' : self.rank
        }
   

    
class UserVo:
    user_id: str = ''
    password: str = ''
    name: str = ''
    pclass: int = 0
    gender: int = 0
    age_group: int = 0
    embarked: int = 0
    rank: int =  0

