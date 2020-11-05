from com_sba_api.ext.db import db

class CabbageDto(db.Model):
    __tablename__='cabbages'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    year: str = db.Column(db.String(10), primary_key = True, index = True)
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
        return f'Cabbage(year= {self.year}, avg_temp={self.avg_temp}, min_temp={self.min_temp}\
            , max_temp={self.max_temp}, rain_fall={self.rain_fall}, avg_price={self.avg_price})'



class CabbageVo:
    year: str = ''
    avg_temp: float = 0.0
    min_temp: float = 0.0
    max_temp: float = 0.0
    rain_fall: float = 0.0
    avg_price: int = 0


