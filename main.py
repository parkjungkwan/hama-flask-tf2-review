from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url, db
from com_sba_api.ext.routes import initialize_routes
from com_sba_api.item.api import Item, Items
from com_sba_api.article.api import Article, Articles
from com_sba_api.user import user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(user)


print(url)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
'''
@app.before_first_request
def create_tables():
    db.create_all()
with app.app_context():
    db.create_all()

from com_sba_api.user.dao import UserDao
UserDao.insert_many()
'''
initialize_routes(api)


