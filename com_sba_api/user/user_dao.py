from com_sba_api.ext.db import db
from com_sba_api.user import User
'''
어플리케이션이 SQLAlchemy ORM을 사용한다면, 
객체에 바인딩된 쿼리를 위해서 Session 객체를 사용해야 한다. 
이는 session.add(), session.rollback(), session.commit(), session.close()를 통해 
트랜잭션을 단일 작업 단위로 관리하기 좋고, 
이러한 특징을 통해 Python의 Context Manager 패턴을 사용하기에도 좋다.
'''
class UserDao(db.Model):

    @classmethod
    def fetch_user_by_id(cls, userid):
        return cls.query.filter_by(userid == userid).first()
        
    @classmethod
    def fetch_all_users(self):
        ...

    

    

