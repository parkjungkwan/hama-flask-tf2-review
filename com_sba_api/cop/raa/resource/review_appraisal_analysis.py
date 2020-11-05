from flask_restful import Resource, reqparse
from com_sba_api.cop.raa.model.review_dao import ReviewDao
from com_sba_api.cop.raa.model.review_dto import ReviewDto, ReviewVo

class ReviewAppraisalAnalysis(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        
    def post(self):
        parser = self.parser
        parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('content', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        review = ReviewDto(args['title'], args['content'],\
                            args['user_id'], args['item_id'])
        try: 
            ReviewDao.save(review)
            return {'code' : 0, 'message' : 'SUCCESS'}, 200    
        except:
            return {'message': 'An error occured inserting the review'}, 500
    @staticmethod
    def get(id):
        review = ReviewDao.find_by_id(id)
        if review:
            return review.json()
        return {'message': 'Review not found'}, 404
    @staticmethod
    def put(self, review, review_id):
        parser = self.parser
        parser.add_argument('art_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('content', type=str, required=False, help='This field cannot be left blank')
        args = parser.parse_args()
        review = ReviewVo()
        review.title = args['title']
        review.content = args['content']
        review.art_id = args['art_id']
        try: 
            ReviewDao.update(review, review_id)
            return {'message': 'Article was Updated successfully'}, 200
        except:
            return {'message': 'An error occured updating the review'}, 500


