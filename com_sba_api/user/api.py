from typing import List
from flask_restful import Resource, reqparse
from com_sba_api.user.dao import UserDao

class User(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    
    def post(self):
        args = self.parser.parse_args()
        print(f'User {args["id"]} added ')
        return {'code':0, 'message': 'SUCCESS'}, 200

    def update(self, id):
        args = self.parser.parse_args()
        print(f'User {args["id"]} updated ')
        return {'code':0, 'message': 'SUCCESS'}, 200

    def delete(self, id):
        args = self.parser.parse_args()
        print(f'USer {args["id"]} deleted')
        return {'code' : 0, 'message' : 'SUCCESS'}, 200

    def get(self, id):
        self.parser.add_argument('id', type=int, required=True,
                                        help='This field should be a Number')
        try:
            user = UserDao.find_by_id(id)
            if user:
                return user.json()
        except Exception as e:
            return {'message': 'User not found'}, 404
    
    

class Users(Resource):
    def __init__(self):
        print('-- 0 --')
        parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    
    @classmethod
    def get():
        ...
    
    def post(self):
        ud = UserDao()
        ud.insert_many('users')




