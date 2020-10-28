from flask_restful import Resource
from flask import Response, jsonify
from com_sba_api.ext.db import db
from flask_restful import Resource, reqparse
from com_sba_api.ext.db import db, openSession
import json
from com_sba_api.resources.user import UserDto
from com_sba_api.resources.item import ItemDto
from com_sba_api.resources.order import OrderDto
from sqlalchemy import func


# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================


class OrderDto(db.Model):
    
       __tablename__ = 'orders'

       order_id = db.Column(db.Integer, primary_key=True)
       user_id = db.Column(db.String(10), db.ForeignKey(UserDto.user_id))
       user = db.relationship('User', back_populates='orders')
       itemId = db.Column(db.Integer, db.ForeignKey('items.id'))
       item = db.relationship('Item', back_populates='orders')
       orderQuantity = db.Column(db.Float)
       orderMeasurement = db.Column(db.String)
       orderPrice = db.Column(db.Float)
       orderDelivery = db.Column(db.Date)
       orderPlaced = db.Column(db.Date)

       def __init__(self, userId, itemId, orderQuantity,
                    orderMeasurement, orderPrice, orderDelivery, orderPlaced):
           self.userId = userId
           self.itemId = itemId
           self.orderQuantity = orderQuantity
           self.orderMeasurement = orderMeasurement
           self.orderPrice = orderPrice
           self.orderDelivery = orderDelivery
           self.orderPlaced = orderPlaced

       def __repr__(self):
           return '<Order {0}>'.format(self.orderDelivery)

Session = openSession()
session = Session()
user_preprocess = UserPreprocess()

class OrderDao(OrderDto):

    @staticmethod   
    def bulk():
        df = user_preprocess.hook()
        print(df.head())
        session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def count():
        return session.query(func.count(UserDto.user_id)).one()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete(cls,id):
        data = cls.query.get(id)
        db.session.delete(data)
        db.session.commit()

    @classmethod
    def find_all(cls):
        sql = cls.query
        df = pd.read_sql(sql.statement, sql.session.bind)
        return json.loads(df.to_json(orient='records'))

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name)

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(user_id == user_id)


    @classmethod
    def login(cls, user):
        sql = cls.query\
            .filter(cls.user_id.like(user.user_id))\
            .filter(cls.password.like(user.password))
        df = pd.read_sql(sql.statement, sql.session.bind)
        print(json.loads(df.to_json(orient='records')))
        return json.loads(df.to_json(orient='records'))
            


if __name__ == "__main__":
    UserDao.bulk()

# ==============================================================
# =======================                  =====================
# =======================    Resource    =======================
# =======================                  =====================
# ==============================================================

parser = reqparse.RequestParser()  
parser.add_argument('userId', type=str, required=True,
                                        help='This field should be a userId')
parser.add_argument('password', type=str, required=True,
                                        help='This field should be a password')

class Order(Resource):
    @staticmethod
    def post():
        args = parser.parse_args()
        print(f'User {args["id"]} added ')
        params = json.loads(request.get_data(), encoding='utf-8')
        if len(params) == 0:

            return 'No parameter'

        params_str = ''
        for key in params.keys():
            params_str += 'key: {}, value: {}<br>'.format(key, params[key])
        return {'code':0, 'message': 'SUCCESS'}, 200

    @staticmethod
    def get(id: str):
        try:
            user = UserDao.find_by_id(id)
            if user:
                return user.json()
        except Exception as e:
            return {'message': 'User not found'}, 404

    @staticmethod
    def update():
        args = parser.parse_args()
        print(f'User {args["id"]} updated ')
        return {'code':0, 'message': 'SUCCESS'}, 200

    @staticmethod
    def delete():
        args = parser.parse_args()
        print(f'USer {args["id"]} deleted')
        return {'code' : 0, 'message' : 'SUCCESS'}, 200    

class Orders(Resource):
    @staticmethod
    def post():
        ud = UserDao()
        ud.bulk('users')
    @staticmethod
    def get():
        data = UserDao.find_all()
        return data, 200

class Auth(Resource):
    @staticmethod
    def post():
        body = request.get_json()
        user = UserDto(**body)
        UserDao.save(user)
        id = user.user_id
        
        return {'id': str(id)}, 200 
