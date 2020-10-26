from flask_restful import Resource, reqparse
from com_sba_api.ext.db import db
from com_sba_api.resources.user import UserDto
from com_sba_api.resources.item import ItemDto

class ArticleDto(db.Model):
    __tablename__ = "articles"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id: int = db.Column(db.Integer, primary_key=True, index=True)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))

    userid: str = db.Column(db.String(30), db.ForeignKey(UserDto.userid))
    item_id: int = db.Column(db.Integer, db.ForeignKey(ItemDto.id))

    def __init__(self, title, content, userid, item_id):
        self.title = title
        self.content = content
        self.userid = userid
        self.item_id = item_id

    def __repr__(self):
        return f'id={self.id}, user_id={self.userid}, item_id={self.item_id},\
            title={self.title}, content={self.content}'

    @property
    def json(self):
        return {
            'id': self.id,
            'userid': self.userid,
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

class ArticleDao(ArticleDto):
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id == id).first()

    @classmethod
    def write_aritcle(cls):
        ...

class Article(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('userid', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('itemid', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('title', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('content', type=str, required=False, help='This field cannot be left blank')

    
    def post(self):
        data = self.parset.parse_args()
        article = ArticleDto(data['title'], data['content'], data['user_id'], data['item_id'])
        print('******************')
        print('******************')
        print('******************')
        print('******************')
        print('******************')
        print(f'{data}')
        try: 
            article.save()
        except:
            return {'message': 'An error occured inserting the article'}, 500
        return article.json(), 201
    
    
    def get(self, id):
        article = ArticleDao.find_by_id(id)
        if article:
            return article.json()
        return {'message': 'Article not found'}, 404

    def put(self, id):
        data = Article.parser.parse_args()
        article = ArticleDao.find_by_id(id)

        article.title = data['title']
        article.content = data['content']
        article.save()
        return article.json()

class Articles(Resource):
    def get(self):
        return {'articles': list(map(lambda article: article.json(), ArticleDao.find_all()))}
        # return {'articles':[article.json() for article in ArticleDao.find_all()]}



    