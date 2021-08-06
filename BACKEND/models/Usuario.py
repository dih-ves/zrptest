from app import db, create_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship 


app = create_app()
db = SQLAlchemy(app)



ACCESS = {
    'user': 0,
    'admin': 1,
    'developer': 7
}

class User(db.Model, UserMixin):
    __tablename__='user'
    
    id = db.Column(db.Integer, primary_key=True)
        
    username = db.Column(db.String(15))
    phone = db.Column(db.String(19))
    email = db.Column(db.String(50), unique=True)
    
    password = db.Column(db.String(80))
    
    access = db.Column(db.Boolean(),default=0)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('User', lazy='dynamic'))

    def is_admin(self):
        return self.access == ACCESS['admin']


    def allowed(self, access_level):
        return self.access >= access_level  


    def get_id(self):
        return self.id

    



# Define the Role data model
class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    


# Define the UserRoles data model
class UserRoles(db.Model):
    __tablename__='user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

        


