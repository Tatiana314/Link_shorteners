import re

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import APIException
from .models import URLMap
from .views import get_unique_short_id

REQUEST_ERROR = 'Отсутствует тело запроса'
URL = '"url" является обязательным полем!'
SHORT_LINK = 'Предложенный вариант короткой ссылки уже существует.'
SHORT_LINK_NAME = 'Указано недопустимое имя для короткой ссылки'
OBJECT_ERROE = 'Указанный id не найден'


@app.route('/api/id/', methods=['POST'])
def short_link():
    data = request.get_json()
    if not data:
        raise APIException(REQUEST_ERROR)
    if 'url' not in data:
        raise APIException(URL)
    if data.get('custom_id'):
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise APIException(SHORT_LINK)
        if not re.match(r'^[a-zA-Z0-9]{1,16}$', data['custom_id']):
            raise APIException(SHORT_LINK_NAME)
    else:
        data['custom_id'] = get_unique_short_id()
        while URLMap.query.filter_by(short=data['custom_id']).count():
            data['custom_id'] = get_unique_short_id()
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        {
            'short_link': url_for('original_link_view', short=url_map.short, _external=True),
            'url': url_map.original
        }), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if original_link:
        return jsonify({'url': original_link.original}), 200
    raise APIException(OBJECT_ERROE, 404)
