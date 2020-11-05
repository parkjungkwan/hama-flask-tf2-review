class ArticleDao(ArticleDto):
    
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filer_by(name == name).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter(ArticleDto.art_id == id).one()

    @staticmethod
    def save(article):
        Session = openSession()
        session = Session()
        session.add(article)
        session.commit()

    @staticmethod
    def update(article, article_id):
        Session = openSession()
        session = Session()
        session.query(ArticleDto).filter(ArticleDto.art_id == article.article_id)\
            .update({ArticleDto.title: article.title,
                        ArticleDto.content: article.content})
        session.commit()

    @classmethod
    def delete(cls,art_id):
        Session = openSession()
        session = Session()
        cls.query(ArticleDto.art_id == art_id).delete()
        session.commit()

            

