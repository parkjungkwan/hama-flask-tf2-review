from com_sba_api.ext.db import db
from com_sba_api.user import User
from com_sba_api.item import Item

class Article(Base):
    __tablename__ = "articles"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id: int = db.Column(db.Integer, primary_key=True, index=True)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))

    user_id: int = db.Column(db.Integer, db.ForeignKey(User.id))
    item_id: int = db.Column(db.Integer, db.ForeignKey(Item.id))

    def __repr__(self):
        return f'id={self.id}, user_id={self.user_id}, item_id={self.item_id},\
            title={self.title}, content={self.content}'

    @property
    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'item_id' : self.item_id,
            'title' : self.title,
            'content' : self.content
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

