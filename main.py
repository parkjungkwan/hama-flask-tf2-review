from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url, db
from com_sba_api.ext.routes import initialize_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

initialize_routes(api)


