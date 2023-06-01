from User import db
from sqlalchemy import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(254), unique=True)
    created_at = db.Column(db.DateTime(), server_default=func.now())
