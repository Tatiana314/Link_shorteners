from http import HTTPStatus
import re

from flask import jsonify, request, url_for

from .constants import LINK_EXISTS

from . import app
from .error_handlers import APIException
from .models import URLMap
from .views import get_unique_short_id

REQUEST_ERROR = 'Отсутствует тело запроса'
URL = '"url" является обязательным полем!'
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
            raise APIException(LINK_EXISTS)
        if not re.match(r'^[a-zA-Z0-9]{1,16}$', data['custom_id']):
            raise APIException(SHORT_LINK_NAME)
    else:
        data['custom_id'] = get_unique_short_id()
    url_map = URLMap.save_link(
        original=data['url'],
        short=data['custom_id']
    )
    return jsonify(
        {
            'short_link': url_for('original_link_view', short=url_map.short, _external=True),
            'url': url_map.original
        }), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if original_link:
        return jsonify({'url': original_link.original}), HTTPStatus.OK
    raise APIException(OBJECT_ERROE, HTTPStatus.NOT_FOUND)
