import datetime
from . import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.String(50), nullable=False)
    profile_photo = db.Column(db.String(255), nullable=False)
    joined_on = db.Column(db.Date, nullable=False, 
                            default=datetime.datetime.now())
    
    followers = db.relationship('UserFollow', backref='User', 
                                    passive_deletes=True, lazy=True)

    def __init__(self, username, password, firstname, lastname, location,
                email, phone_number, profile_photo):
                    
        self.username = username
        self.password = generate_password_hash(
                            password, 
                            method='pbkdf2:sha256'
                        )
        self.firstname = firstname
        self.lastname = lastname
        self.location = location
        self.email = email
        self.phone_number = phone_number
        self.profile_photo = profile_photo
