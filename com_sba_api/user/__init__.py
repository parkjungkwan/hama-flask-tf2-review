import logging
from flask import Blueprint
from flask_restful import Api
from com_sba_api.user.api import User

user = Blueprint('user', __name__, url_prefix='/api/user')
api = Api(user)

api.add_resource(User, '/api/user/<user_key>')


@user.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during user request. %s' % str(e))
    return 'An internal error occurred.', 500