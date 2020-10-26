from flask_restful import Resource, reqparse
from com_sba_api.ext.db import db, openSession
from com_sba_api.resources.user import UserDto
from com_sba_api.resources.item import ItemDto

class ArticleDto(db.Model):
    __tablename__ = "articles"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    art_id: int = db.Column(db.Integer, primary_key=True, index=True)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))

    user_id: str = db.Column(db.String(30), db.ForeignKey(UserDto.user_id))
    item_id: int = db.Column(db.Integer, db.ForeignKey(ItemDto.item_id))

    def __init__(self, title, content, user_id, item_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.item_id = item_id

    def __repr__(self):
        return f'art_id={self.art_id}, user_id={self.user_id}, item_id={self.item_id},\
            title={self.title}, content={self.content}'

    @property
    def json(self):
        return {
            'art_id': self.art_id,
            'user_id': self.user_id,
            'item_id' : self.item_id,
            'title' : self.title,
            'content' : self.content
        }

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

    @staticmethod
    def save(article):
        print('# ==============================================================')
        print(article)
        Session = openSession()
        session = Session()
        newArticle = ArticleDto(title = article['user_id'], 
                                content = article['content'], 
                                user_id = article['user_id'], 
                                item_id = article['item_id'])
        session.add(newArticle)
        session.commit()

    @staticmethod
    def modify(article):
        Session = openSession()
        session = Session()
        session.add(article)
        session.commit()

    @classmethod
    def delete(cls,art_id):
        Session = openSession()
        session = Session()
        data = cls.query.get(art_id)
        session.delete(data)
        session.commit()

# ==============================================================
# ==============================================================
# ====================     Controller  ========================
# ==============================================================
# ==============================================================


parser = reqparse.RequestParser()
parser.add_argument('user_id', type=int, required=False, help='This field cannot be left blank')
parser.add_argument('item_id', type=int, required=False, help='This field cannot be left blank')
parser.add_argument('title', type=str, required=False, help='This field cannot be left blank')
parser.add_argument('content', type=str, required=False, help='This field cannot be left blank')
class Article(Resource):
        
    @staticmethod    
    def post():
        args = parser.parse_args()
        article = ArticleDto(args['title'], args['content'],\
             args['user_id'], args['item_id'])
        print('******************')
        print('******************')
        print('******************')
        print('******************')
        print('******************')
        print(f'{args}')
        try: 
            ArticleDao.save(args)
            return {'code' : 0, 'message' : 'SUCCESS'}, 200    
        except:
            return {'message': 'An error occured inserting the article'}, 500
        
    
    
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



    