from typing import List
from flask_restful import Resource, reqparse
from com_sba_api.user.dao import UserDao

class User(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
        parser.add_argument('store_id', type=int, required=True, help='Must enter the store id')

    @classmethod
    def get(cls, name):
        item = cls.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    

class Users(Resource):
    def __init__(self):
        print('-- 0 --')
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
        parser.add_argument('price', type=float, required=True, help='This field cannot be left blank')
        parser.add_argument('store_id', type=int, required=True, help='Must enter the store id')
    
    @classmethod
    def get():
        ...
    
    def post(self):
        print('-- 9 --')
        ud = UserDao()
        ud.insert_many('users')




