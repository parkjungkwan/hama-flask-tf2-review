import logging
from flask import Blueprint
from flask_restful import Api
from com_sba_api.cmm.hom.resource.home import Home
from com_sba_api.cop.cab.resource.cabbage import Review, Reviews
from com_sba_api.cop.rvw.resource.review import Review, Reviews
from com_sba_api.cop.itm.resource.item import Item, Items
from com_sba_api.cop.sto.resource.stock import Stock, Stocks
from com_sba_api.usr.resource.user import User, Users
from com_sba_api.usr.resource.access import Access
from com_sba_api.cop.rvw.model.review_dto import ReviewVo
from com_sba_api.resources.cabbage import Cabbage

home = Blueprint('home', __name__, url_prefix='/api')
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
access = Blueprint('access', __name__, url_prefix='/api/access')
article = Blueprint('article', __name__, url_prefix='/api/article')
articles = Blueprint('articles', __name__, url_prefix='/api/articles')
cabbage = Blueprint('cabbage', __name__, url_prefix='/api/cabbage')

api = Api(home)
api = Api(user)
api = Api(users)
api = Api(access)
api = Api(article)
api = Api(articles)

def initialize_routes(api):
    review = ReviewVo()

    api.add_resource(TodoNext, '/next', resource_class_kwargs={ 'smart_engine': smart_engine })
    api.add_resource(Home, '/api')
    api.add_resource(Item, '/api/item', '/api/item/<item_id>')
    api.add_resource(Items,'/api/items')
    api.add_resource(User, '/api/user', '/api/user/<user_id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Access, '/api/access')
    api.add_resource(Review, '/api/review', resource_class_kwargs={ 'review': review })
    api.add_resource(Reviews, '/api/articles/')
    api.add_resource(Cabbage, '/api/cabbage')

@user.errorhandler(500)
def user_api_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500

@home.errorhandler(500)
def home_api_error(e):
    logging.exception('An error occurred during home request. %s' % str(e))
    return 'An internal error occurred.', 500

@article.errorhandler(500)
def article_api_error(e):
    logging.exception('An error occurred during article request. %s' % str(e))
    return 'An internal error occurred.', 500

@cabbage.errorhandler(500)
def cabbage_api_error(e):
    logging.exception('An error occurred during cabbage request. %s' % str(e))
    return 'An internal error occurred.', 500