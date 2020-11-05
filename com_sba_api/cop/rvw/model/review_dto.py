from flask_restful import Resource, reqparse
from com_sba_api.ext.db import db, openSession
from com_sba_api.resources.user import UserDto
from com_sba_api.resources.item import ItemDto

class ReviewDto(db.Model):
    __tablename__ = "reviews"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    rvw_id: int = db.Column(db.Integer, primary_key=True, index=True)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))

    user_id = db.Column(db.String(10), db.ForeignKey(UserDto.user_id))
    user = db.relationship('UserDto', back_populates='articles')
    item_id = db.Column(db.Integer, db.ForeignKey(ItemDto.item_id))
    item = db.relationship('ItemDto', back_populates='articles')

    def __init__(self, title, content, user_id, item_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.item_id = item_id

    def __repr__(self):
        return f'rvw_id={self.rvw_id}, user_id={self.user_id}, item_id={self.item_id},\
            title={self.title}, content={self.content}'

    def json(self):
        return {
            'rvw_id': self.rvw_id,
            'user_id': self.user_id,
            'item_id' : self.item_id,
            'title' : self.title,
            'content' : self.content
        }
class ReviewVo():
    rvw_id: int = 0
    user_id: str = ''
    item_id: int = 0
    title: str = ''
    content: str = ''
