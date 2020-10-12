import mysql.connector
from com_sba_api.ext.db import config

class FoodDao:
    
    def __init__(self):
        self.connector  = mysql.connector.connect(**config)
        self.cursor = self.connector.cursor(dictionary=True)


    def select_foods(self):
        cur = self.cursor
        con = self.connector

        try:
            cur.execute('select * from food',)
            for row in cur:
                print(f'price is : {str(row["price"])}')
            cur.close()
        except:
            print('Exception ...')

        finally:
            if con is not None:
                con.close()

print('---2---')
dao = FoodDao()
dao.select_foods()
    
    
    