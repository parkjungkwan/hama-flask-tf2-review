from com_sba_api.ext.db import db 
# from com_stock_api.kospi_pred.dto import KospiDto
# from com_stock_api.korea_covid.dto import KoreaDto
# from com_stock_api.naver_finance.dto import StockDto

class NewsDto(db.Model):
    __tablename__ = 'naver_news'
    __table_args__ = {'mysql_collate':'utf8_general_ci'}
    
    news_id : int = db.Column(db.String(30), primary_key = True, index=True)
    date : datetime = db.Column(db.datetime)
    sentiment_analysis :str = db.Column(db.String(30))
    keywords :str = db.Column(db.String(30))
    
    def __init__(self, news_id, date, sentiment_analysis, keywords):
        self.news_id = news_id
        self.date = date
        self.sentiment_analysis = sentiment_analysis
        self.keywords = keywords
        
    
    def __repr__(self):
        return f'news_id={self.news_id}, date={self.date}, sentiment_analysis={self.sentiment_analysis},\
            keywords={self.keywords}'
            
    @property
    def json(self):
        return {
            'news_id': self.news_id,
            'date': self.date,
            'sentiment_analysis' : self.sentiment_analysis,
            'keywords' : self.keywords
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()