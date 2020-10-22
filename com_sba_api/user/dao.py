from com_sba_api.ext.db import db, openSession
from com_sba_api.user.service import UserService
from com_sba_api.user.dto import UserDto

class UserDao(object):
    def __init__(self):
        ...
        

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.filter_by(userid == userid).first()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod   
    def insert_many():
        service = UserService()
        Session = openSession()
        session = Session()
        df = service.hook()
        print(df.head())
        session.bulk_insert_mappings(UserDto, df.to_dict(orient="records"))
        session.commit()
        session.close()

    @staticmethod
    def modify_user(user):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete_user(cls,id):
        data = cls.query.get(id)
        db.session.delete(data)
        db.session.commit()
        
    

'''    
u = UserDao()
u.insert_many()
'''