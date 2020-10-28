from flask_restful import Resource
from flask import Response, jsonify
from com_sba_api.ext.db import db

class ItemService(object):
    ...


# ==============================================================
# ==========================             =======================
# ==========================    Model    =======================
# ==========================             =======================
# ==============================================================


class ItemDto(db.Model):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    item_id : int = db.Column(db.Integer, primary_key=True, index=True)
    item_name : str = db.Column(db.String(30))
    measurement = db.Column(db.String, nullable=True)
    default_price = db.Column(db.Float, nullable=True)
    minimum_order = db.Column(db.Float, nullable=True)
    maximum_order = db.Column(db.Float, nullable=True)
    orders = db.relationship('Order', back_populates='item')
    prices = db.relationship('Price', back_populates='item')
    articles = db.relationship('ArticleDto', lazy='dynamic')

    def __init__(self, item_name, measurement, default_price,
                    minimum_order, maximum_order):
        self.item_name = item_name
        self.default_price = default_price
        self.item_name = item_name
        self.measurement = measurement
        self.default_price = default_price
        self.minimum_order = minimum_order
        self.maximum_order = maximum_order
        


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

class ItemDao(ItemDto):
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id == id).first()





# ==============================================================
# ====================                  ========================
# ====================     RESOURCE     ========================
# ====================                  ========================
# ==============================================================



class Item(Resource):
    ...

class Items(Resource):
    ... 

