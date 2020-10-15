import mysql.connector
from com_sba_api.ext.db import config

class ArticleDao(object):
    def __init__(self):
        self.connector = mysql.connector.connect(**config)
        self.cursor = self.connector.cursor(dictionary= True)

    
