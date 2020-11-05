from flask_restful import Resource, reqparse
from com_sba_api.cop.raa.model.review_dao import ReviewDao

class Articles(Resource):
    def get(self):
        return {'articles': list(map(lambda article: article.json(), ReviewDao.find_all()))}
        # return {'articles':[article.json() for article in ArticleDao.find_all()]}