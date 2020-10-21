from com_sba_api.ext.db import Base, Session, engine
from com_sba_api.user.service import UserService
import time

'''
pip install sqlalchemy-easy-profile
'''
class UserDao(object):
    def __init__(self):
        global engine
        Session.configure(bind=engine, autoflush=False, expire_on_commit=False)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        
        

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.filter_by(userid == userid).first()

    
    def insert_many(cls, table, n = 10000):
        print('-- 2 --')
        service = UserService()
        df = service.hook()
        print(df)
        t0 = time.time()
        Session = sessionmaker(bind=dest_db_con)
        Session.bulk_insert_mappings(cls,
                                    table[:n].to_dict(orient="record"))

        Session.commit()
        print("SQLAlchemy ORM bulk_insert_mappings(): Total time for " + str(n) +
            " records " + str(time.time() - t0) + " secs")
        
    

    

    

