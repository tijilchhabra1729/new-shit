from hack import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String(64),index=True)
    password = db.Column(db.String)
    
class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    url = db.Column(db.String)
    img = db.Column(db.String)
    sizes = db.relationship('Size')

class Size(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer)
    sneaker = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
    
# class Company(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     snkr = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
    
# class Price(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.String)
#     snkr = db.Column(db.Integer, db.ForeignKey('sneaker.id'))
