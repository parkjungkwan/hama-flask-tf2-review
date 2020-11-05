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
from com_sba_api.usr.model.user_dto import UserDto
from com_sba_api.usr.model.user_dao import UserDao
'''
json = json.loads() => dict
dict = json.dumps() => json
'''


parser = reqparse.RequestParser() 

class User(Resource):
    @staticmethod
    def post():
        print(f'[ User Signup Resource Enter ] ')
        body = request.get_json()
        user = UserDto(**body)
        UserDao.save(user)
        user_id = user.user_id
        
        return {'userId': str(user_id)}, 200 

    @staticmethod
    def get(userId: str):
        try:
            print(f'User ID is {userId} ')
            user = UserDao.find_one(userId)
            if user:
                return json.dumps(user.json()), 200
        except Exception as e:
            return {'message': 'User not found'}, 404


    @staticmethod
    def put():
        print(f'[ User Put Resource Enter ] ')
        parser.add_argument('userId')
        parser.add_argument('password')
        parser.add_argument('pclass')
        parser.add_argument('embarked')
        args = parser.parse_args()
        UserDao.update(args)
        user = UserDao.find_one(args.userId)
        if args.password == user.password and\
        args.pclass == user.pclass and\
        args.embarked == user.embarked :
            print(f'User Update Success')
            return user.json(), 200
        else: 
            print(f'User Update Failure')
            return {'message': 'User not found'}, 404
        

    @staticmethod
    def delete():
        print(f'[ User Delete Resource Enter ] ')
        args = parser.parse_args()
        print(f'User {args["userId"]} deleted')
        return {'code' : 0, 'message' : 'SUCCESS'}, 200    

class Users(Resource):
            
    @staticmethod
    def post():
        print(f'[ User Bulk Resource Enter ] ')
        UserDao.bulk()
    @staticmethod
    def get():
        print(f'[ User List Resource Enter ] ')
        data = UserDao.find_all()
        return json.dumps(data), 200
