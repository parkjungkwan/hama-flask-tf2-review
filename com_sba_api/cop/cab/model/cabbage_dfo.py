

class CabbageDfo(object):
    def __init__(self):
        self.fileReader = FileReader()  
        self.data = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
        self.dfo = None

    def new_train(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'{self.data}')
        print(f'{this.fname}')
        return pd.read_csv(Path(self.data, this.fname)) 

    def create(self):
        this = self.fileReader
        price_data = 'price_data.csv'
        this.train = self.new_train(price_data)
        print(this.train.columns)
        '''
        Index(['year', 'avgTemp', 'minTemp', 'maxTemp', 'rainFall', 'avgPrice'], dtype='object')
        '''
        self.dfo = pd.DataFrame(

            {
             'year' : this.train.year,
             'avg_temp' : this.train.avgTemp,
             'min_temp' : this.train.minTemp,
             'max_temp' : this.train.maxTemp,
             'rain_fall' : this.train.rainFall,
             'avg_price' : this.train.avgPrice
             }
        )
        return self.dfo
    
    
    
    

'''
CabbageDF.new()
          year  avgTemp  minTemp  maxTemp  rainFall  avgPrice
0     20100101     -4.9    -11.0      0.9       0.0      2123
1     20100102     -3.1     -5.5      5.5       0.8      2123
2     20100103     -2.9     -6.9      1.4       0.0      2123
3     20100104     -1.8     -5.1      2.2       5.9      2020
4     20100105     -5.2     -8.7     -1.8       0.7      2060
...        ...      ...      ...      ...       ...       ...
2917  20171227     -3.9     -8.0      0.7       0.0      2865
2918  20171228     -1.5     -6.9      3.7       0.0      2884
2919  20171229      2.9     -2.1      8.0       0.0      2901
2920  20171230      2.9     -1.6      7.1       0.6      2901
2921  20171231      2.1     -2.0      5.8       0.4      2901

[2922 rows x 6 columns]


from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = {
    'user' : 'root',
    'password' : 'root',
    'host': '127.0.0.1',
    'port' : '3306',
    'database' : 'com_sba_api'
}
charset = {'utf8':'utf8'}
url = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8"
Base = declarative_base()
engine = create_engine(url)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

       year  avg_temp  min_temp  max_temp  rain_fall  avg_price
0  20100101      -4.9     -11.0       0.9        0.0       2123
1  20100102      -3.1      -5.5       5.5        0.8       2123
2  20100103      -2.9      -6.9       1.4        0.0       2123
3  20100104      -1.8      -5.1       2.2        5.9       2020
4  20100105      -5.2      -8.7      -1.8        0.7       2060
'''

