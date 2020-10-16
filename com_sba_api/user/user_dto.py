from com_sba_api.ext.db import db

class UserModel(db.Model):

    __tablename__ = 'users'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    userid = db.Column(db.String(30), primary_key = True, index = True)
    password = db.Column(db.String(30))
    name = db.Column(db.String(30))

    def __repr__(self):
        return f'User(id={self.id},userid={self.userid},\
            password={self.password},name={self.name})'

    @property
    def json(self):
        return {
            'userid' : self.userid,
            'password' : self.password,
            'name' : self.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class UserDto(object):
    userid: str
    password: str
    name: str


