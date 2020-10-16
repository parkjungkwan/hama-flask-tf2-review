from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from com_sba_api.ext.db import Base

class Item(Base):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)

    def __repr__(self):
        return f''

class ItemDto(BaseModel):
    id: int
    name: str
    price: str





    