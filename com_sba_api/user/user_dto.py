from sqlalchemy import Column, Integer 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR, LONGTEXT

class User(Base):

    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id = Column(Integer, primary_key = True, index = True)
    userid = Column(VARCHAR(30))
    password = Column(VARCHAR(30))
    name = Column(VARCHAR(30))

    def __repr__(self):
        return f'User(id={self.id},userid={self.userid},\
            password={self.password},name={self.name})'

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name
        }



class UserDto(object):
    id: int
    userid: str
    password: str
    name: str


