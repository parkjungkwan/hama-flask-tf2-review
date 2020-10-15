from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from com_sba_api.ext.db import Base
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
        return f'User(id=\'{self.id}\',userid=\'{self.userid}\',\
            password=\'{self.password}\',name=\'{self.name}\',)'



engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.add(User(userid='tom', password='1', name='thomas'))
query = session.query(User).filter((User.userid == 'tom'))
print(query)
for i in query:
    print(i)
    
session.commit()