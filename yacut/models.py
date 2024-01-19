import re
from datetime import datetime
from random import choices

from . import db
from .constants import (LEN_SHORT, LINK_EXISTS, MAX_LEN_ORIGINAL_LINK,
                        MAX_LEN_SHORT, SHORT_LINK_NAME, SHORT_LINK_SIMBOLS)

FIELD_LENGTH_ERROR = (
    'Поле должно содержать не более {MAX_LEN_ORIGINAL_LINK} символов.'
)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.original}, {self.short}, {self.timestamp}'

    @staticmethod
    def save_link(short, original):
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
    
    @staticmethod
    def save(url_map):
        db.session.add(url_map)
        db.session.commit()

    @staticmethod
    def get_object(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_unique_short():
        short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
        while URLMap.query.filter_by(short=short).count():
            short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
        return short

    @staticmethod
    def validate_on_save(short, original):
        if len(original) > MAX_LEN_ORIGINAL_LINK:
            raise ValueError(FIELD_LENGTH_ERROR)
        if short:
            if URLMap.get_object(short=short):
                raise ValueError(LINK_EXISTS)
            if (len(short) > MAX_LEN_SHORT or
                    not re.match(f'^[{SHORT_LINK_SIMBOLS}]+$', short)):
                raise ValueError(SHORT_LINK_NAME)
        else:
            short = URLMap.get_unique_short()
        url_map = URLMap.save_link(
            original=original,
            short=short
        )
        return url_map
