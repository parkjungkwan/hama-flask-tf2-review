import mysql.connector
from com_sba_api.ext.db import config
from com_sba_api.user.user_dao import UserDao
from com_sba_api.item.item_dao import ItemDao
from com_sba_api.article.article_dao import ArticleDao

class HomeDao():
    def __init__(self):
        self.user_dao = UserDao()
        self.article_dao = ArticleDao()
        self.item_dao = ItemDao()

    def create_tables(self):
        ...

