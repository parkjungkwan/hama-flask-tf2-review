from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()
Base = declarative_base()
config = {
    'user' : 'root',
    'password' : 'root',
    'host': 'localhost',
    'port' : '3306',
    'database' : 'mariadb'
}
charset = {'utf8':'utf8'}
url = f"mysql+mysqlconnector://{config['user']}:{config['password']}\
    @config['host']/config['database']?charset={charset['utf8']}"
def openSession():
    ...
