from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager. writer_loader
def load_Writer(Writer_id):
    return Writer.query.get(int(Writer_id))

        
class Writer(UserMixin,db.Model):
    __tablename__ = 'writers'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    blog = db.relationship('Blog',backref = 'writer',lazy="dynamic")
    comments= db.relationship('Comment', backref= 'writer', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
   
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'Writer {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String)
    author = db.Column(db.String(255))
    # delete = db.Column(db.Integer)
    # update = db.Column(db.Integer)        
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    
class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)    
    body = db.Column(db.String)          
    published_at = db.Column(db.DateTime, default = datetime.utcnow)    
    writer_id = db.Column(db.Integer, db.ForeignKey('writers.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

class Email(db.Model):
    __tablename__ = 'emails'

    id = db.Column(db.Integer, primary_key = True)    
    user_email = db.Column(db.String)          
    username = db.Column(db.String)   
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
