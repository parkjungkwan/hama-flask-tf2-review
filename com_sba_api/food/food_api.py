from flask_restful import Resource
from com_sba_api.food.food_dao import FoodDao

class FoodsApi(Resource):
    def get(self):
       dao = FoodDao()
        