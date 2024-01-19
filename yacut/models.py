import re
from datetime import datetime
from random import choices

from . import db
from .constants import (LEN_SHORT, LINK_EXISTS, MAX_LEN_ORIGINAL_LINK,
                        MAX_LEN_SHORT, REGEX, REQUEST_ERROR, SHORT_LINK_NAME,
                        SHORT_LINK_SIMBOLS, URL)
from .error_handlers import APIException


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.original}, {self.short}, {self.timestamp}'

    def from_dict(self, data):
        self.original = data['url']
        self.short = data['custom_id']

    @classmethod
    def save_link(cls, short, original):
        url_map = cls(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def get_unique_short():
        short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
        while URLMap.query.filter_by(short=short).count():
            short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
        return short

    @staticmethod
    def validate_on_save(data):
        if not data:
            raise APIException(REQUEST_ERROR)
        if 'url' not in data:
            raise APIException(URL)
        if data.get('custom_id'):
            if URLMap.query.filter_by(short=data['custom_id']).first():
                raise APIException(LINK_EXISTS)
            if not re.match(REGEX, data['custom_id']):
                raise APIException(SHORT_LINK_NAME)
        else:
            data['custom_id'] = URLMap.get_unique_short()
        url_map = URLMap.save_link(
            original=data['url'],
            short=data['custom_id']
        )
        return url_map
