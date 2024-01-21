import re
from datetime import datetime
from random import choices

from . import db
from .constants import (ITERATIONS, LEN_SHORT, MAX_LEN_ORIGINAL_LINK,
                        MAX_LEN_SHORT, REGEX, SHORT_LINK_SIMBOLS)

FIELD_LENGTH_ERROR = (
    'Поле должно содержать не более {MAX_LEN_ORIGINAL_LINK} символов.'
)
GENERATION = 'Превышен лимит генерации короткой ссылки.'
LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
SHORT_LINK_NAME = 'Указано недопустимое имя для короткой ссылки'


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL_LINK), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f'{self.id}, {self.original}, {self.short}, {self.timestamp}'

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_or_404(short):
        return URLMap.query.filter_by(short=short).first_or_404()

    @staticmethod
    def get_unique_short_id():
        for _ in range(ITERATIONS):
            short = ''.join(choices(SHORT_LINK_SIMBOLS, k=LEN_SHORT))
            if URLMap.get(short=short):
                break
        if short:
            return short
        raise ValueError(GENERATION)

    @staticmethod
    def save(short, original, api=True):
        if api and len(original) > MAX_LEN_ORIGINAL_LINK:
            raise ValueError(FIELD_LENGTH_ERROR)
        if short:
            if api and (len(short) > MAX_LEN_SHORT or
                not re.match(REGEX, short)):
                raise ValueError(SHORT_LINK_NAME)
            if api and URLMap.get(short=short):
                raise ValueError(LINK_EXISTS)
        else:
            short = URLMap.get_unique_short_id()
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
