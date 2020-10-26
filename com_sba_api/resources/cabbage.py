
from typing import List
from flask import request
from flask_restful import Resource, reqparse
import json
from flask import jsonify
from com_sba_api.ext.db import db, openSession
import pandas as pd
import json
import os
from com_sba_api.util.file import FileReader
import pandas as pd
import numpy as np
from pathlib import Path
from sqlalchemy import func
class CabbageDto(db.Model):
    __tablename__='cabbages'
    __table_args__={'mysql_collate':'utf8_general_ci'}
    # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice

    cab_id: int = db.Column(db.Integer, primary_key = True, index = True)
    year: str = db.Column(db.String(4))
    avg_temp: float = db.Column(db.Float)
    min_temp: float = db.Column(db.Float)
    max_temp: float = db.Column(db.Float)
    rain_fall: float = db.Column(db.Float)
    avg_price: int = db.Column(db.Integer)

    def __init__(self, year, avg_temp, min_temp, max_temp, rain_fall, avg_price):
        self.year = year
        self.avg_temp = avg_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.rain_fall = rain_fall
        self.avg_price = avg_price

    def __repr__(self):
        return f'Cabbage(cab_id= {self.cab_id})'

class CabbageVo:
    year: str = ''
    avg_temp: float = 0.0
    min_temp: float = 0.0
    max_temp: float = 0.0
    rain_fall: float = 0.0
    avg_price: int = 0

class CabbageService:
    def hook(self):
        ...

Session = openSession()
session = Session()
service = CabbageService()

class CabbageDao(CabbageDto):
    @staticmethod
    def bulk():
        
        df = service.hook()
        session.bulk_insert_mapping(CabbageDto, df.to_dict(orient='records'))
        session.commit()
        session.close()

    @classmethod
    def count(cls):
        # return cls.query.count()
        return session.query(func.count(CabbageDto.cab_id))

    @staticmethod
    def save(cabbage):
        Session = openSession()
        session = Session()
        newCabbage = CabbageDto(year= cabbage['year'],
                                avg_temp= cabbage['avg_temp'],
                                min_temp= cabbage['min_temp'],
                                max_temp= cabbage['max_temp'],
                                rain_fall= cabbage['rain_fall'],
                                avg_price= cabbage['avg_price'])
        session.add(newCabbage)
        session.commit() 

    @classmethod
    def update(cls, cabbage):
        cls.query.filter_by(cab_id=cabbage.cab_id).update({})


                            
    

    





    








