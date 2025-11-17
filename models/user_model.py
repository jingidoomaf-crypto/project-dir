from models.db import db
from datetime import datetime, timezone

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))  
    lname = db.Column(db.String(50))
    email = db.Column(db.String(255), unique=True)
    pass_word = db.Column(db.String(255))  
    birthday = db.Column(db.Date)
    gender = db.Column(db.String(10))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    student_id = db.Column(db.String(50), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User {self.email}>"
