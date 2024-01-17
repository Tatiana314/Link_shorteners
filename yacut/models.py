from datetime import datetime

from . import db


class URLMap(db.Model):
    __tablename__ = 'url_maps'
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.original}, {self.short}, {self.timestamp}'

    def from_dict(self, data):
        self.original = data['url']
        self.short = data['custom_id']
