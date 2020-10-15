from flask_restful import Resource
from flask import Response, jsonify
from com_sba_api.item.item_dao import ItemDao
from fastapi import ApiRouter, HTTPExceiption


class ItemApi(Resource):

    def __init__(self):
        self.api = ApiRouter()
        self.dao = ItemDao()

  

        