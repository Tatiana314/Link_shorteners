from datetime import datetime

from .constants import MAX_LEN_ORIGINAL_LINK, MAX_LEN_SHORT

from . import db


class URLMap(db.Model):
    __tablename__ = 'url_maps'
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.original}, {self.short}, {self.timestamp}'

    def from_dict(self, data):
        self.original = data['url']
        self.short = data['custom_id']

    @staticmethod
    def norm2(x, y):
        return x*x + y*y
