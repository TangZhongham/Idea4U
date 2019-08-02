from idea4u import db
from datetime import datetime


class Idea(db.Model):
    """点子类"""
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(10))
    idea = db.Column(db.String(50))
    writer = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)