from com_sba_api.ext.db import db

class ItemModel(db.Model):
    __tablename__='items'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(30))
    price = db.Column(db.String(30))

    articles = db.relationship('ArticleModel', lazy='dynamic')

    def __repr__(self):
        return f''

class ItemDto(object):
    id: int
    name: str
    price: str





    