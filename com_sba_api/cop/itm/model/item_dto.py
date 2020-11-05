from com_sba_api.ext.db import db
from flask_restful import Resource
from flask import Response, jsonify
from flask_restful import Resource, reqparse
import json


class ItemDto(db.Model):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    item_id : int = db.Column(db.Integer, primary_key=True, index=True)
    item_name : str = db.Column(db.String(30))
    default_price = db.Column(db.Integer, nullable=True)

    #orders = db.relationship('OrderDto', back_populates='item', lazy='dynamic')
    #prices = db.relationship('PriceDto', back_populates='item', lazy='dynamic')
    articles = db.relationship('ReviewDto', back_populates='item', lazy='dynamic')

    def __init__(self, item_name, default_price):
        self.item_name = item_name
        self.default_price = default_price


    def __repr__(self):
        return f'Item(item_id={self.item_id}, item_name={self.item_name},\
             default_price={self.default_price})'

    @property
    def json(self):
        return {'itemId': self.item_id, 'item_name': self.item_name, 'default_price': self.default_price}

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


        
class ItemVo():
    ...