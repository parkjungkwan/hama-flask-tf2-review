from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url, db
from com_sba_api.ext.routes import initialize_routes
from com_sba_api.resources.user import UserDao
from flask_cors import CORS

    

app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)
with app.app_context():
    db.create_all()
with app.app_context():
    count = UserDao.count()
    print(f'Users Total Count is {count}')
    if count == 0:
        UserDao.insert_many()

initialize_routes(api)


