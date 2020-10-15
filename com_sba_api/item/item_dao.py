import mysql.connector
from com_sba_api.ext.db import config
from sqlalchemy.orm import Session
from com_sba_api.item.item_dto import ItemDto, Item

class ItemDao(object):
    
    def __init__(self):
        self.connector  = mysql.connector.connect(**config)
        self.cursor = self.connector.cursor(dictionary=True)

    def add_item(self, db: Session, param: ItemDto):
        item = Item(name=param.name, price=param.price)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item

    def get_all_items(self, db: Session):
        return db.query(Item).all()

    def get_item_by_id(self, db: Session, param: int):
        return db.query(Item).filter(Item.id == param).first()

    def delete_item_by_id(self, db: Session, param: int):
        result = db.query(Item).filter(Item.id == param).first()
        db.delete(result)
        db.commit()

    
    