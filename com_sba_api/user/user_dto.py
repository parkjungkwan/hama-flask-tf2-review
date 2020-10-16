from sqlalchemy import Column, Integer, String,  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class User(Base):

    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    userid = Column(String(30), primary_key = True, index = True)
    password = Column(String(30))
    name = Column(String(30))

    def __repr__(self):
        return f'User(id={self.id},userid={self.userid},\
            password={self.password},name={self.name})'

    @property
    def serialize(self):
        return {
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name
        }



class UserDto(object):
    userid: str
    password: str
    name: str


