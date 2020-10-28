from flask_restful import Resource
from flask import Response, jsonify
from com_sba_api.ext.db import db
from com_sba_api.resources.item import ItemDto
from com_sba_api.resources.user import UserDto
# ==============================================================
# =======================                =======================
# =======================    Modeling    =======================
# =======================                =======================
# ==============================================================

class Price(db.Model):
    
       __tablename__ = 'prices'

       price_id = db.Column(db.Integer, primary_key=True)
       user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
       user = db.relationship('User', back_populates='prices')
       item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
       item = db.relationship('Item', back_populates='prices')
       available = db.Column(db.Boolean)
       price_measurement = db.Column(db.String)
       price = db.Column(db.Float)

       def __init__(self, userId, itemId, priceMeasurement, price):
           self.userId = userId
           self.itemId = itemId
           self.priceMeasurement = priceMeasurement
           self.price = price

       def __repr__(self):
           return '<Price {0}>'.format(self.price)

# ==============================================================
# =====================                  =======================
# =====================    Resourcing    =======================
# =====================                  =======================
# ==============================================================
