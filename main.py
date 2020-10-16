from flask import Flask
from flask_restful import Api
from com_sba_api.ext.db import url
from com_sba_api.ext.routes import initialize_routes
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

initialize_routes(api)

if __name__ == '__main__':
    from com_sba_api.ext.db import db  #Avoid circular import
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True