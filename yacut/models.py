from datetime import datetime

from .constants import MAX_LEN_ORIGINAL_LINK, MAX_LEN_SHORT, SHORT_LINK_SIMBOLS

from . import db


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

    def save(self):
        db.session.add(self)
        db.session.commit()


    # @cmethod
    # def norm2(short, original):
    #     if short:
    #         if URLMap.query.filter_by(short=short).first():
    #             raise APIException(SHORT_LINK_NAME)
    #     if not re.match(r'^[a-zA-Z0-9]{1,16}$', short):
    #         raise APIException(SHORT_LINK_NAME)
    #     # else:
    #     #  #   short = get_unique_short_id()
    #     #     while URLMap.query.filter_by(short=short).count():
    #     #        # short = get_unique_short_id()
    #     #         url_map = URLMap()
    #     # url_map.from_dict(short, original)
    #     # # db.session.add(url_map)
    #     # # db.session.commit()
    #     # return url_map
