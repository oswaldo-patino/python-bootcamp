from datetime import datetime
from . import db

class Channel(db.Model):
    """"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500), nullable=False)

    entries = db.relationship('Entry', back_populates='channel', lazy=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Entry(db.Model):
    """"""
    id = db.Column(db.Text, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text)
    views = db.Column(db.Integer, nullable=False, default=0)

    channel_id = db.Column(db.Integer, db.ForeignKey("channel.id"), nullable=False)
    channel = db.relationship('Channel', back_populates="entries", lazy=True)

    def __str__(self) -> str:
        return f"{self.channel.name} -> {self.title}"