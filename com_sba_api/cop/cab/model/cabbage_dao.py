from com_sba_api.cop.cpp.model.cabbage_dto import CabbageDto
from com_sba_api.cop.cpp.model.cabbage_dfo import CabbageDfo
from com_sba_api.ext.db import openSession
from sqlalchemy import func

Session = openSession()
session = Session()
class CabbageDao(CabbageDto):

    @staticmethod
    def bulk():
        
        cabbage_df = CabbageDfo()
        df = cabbage_df.create()
        print(df.head())
        session.bulk_insert_mappings(CabbageDto, df.to_dict(orient='records'))
        session.commit()
        session.close()

    @staticmethod
    def count():
        return session.query(func.count(CabbageDto.year)).one()

    @staticmethod
    def save(cabbage):
        new_cabbage = CabbageDto(year= cabbage['year'],
                                avg_temp= cabbage['avg_temp'],
                                min_temp= cabbage['min_temp'],
                                max_temp= cabbage['max_temp'],
                                rain_fall= cabbage['rain_fall'],
                                avg_price= cabbage['avg_price'])
        session.add(new_cabbage)
        session.commit() 
