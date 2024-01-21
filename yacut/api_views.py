from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .constants import ORIGINAL_LINK_VIEW
from .error_handlers import APIException
from .models import URLMap

OBJECT_ERROR = 'Указанный id не найден'
REQUEST_ERROR = 'Отсутствует тело запроса'
URL = '"url" является обязательным полем!'


@app.route('/api/id/', methods=['POST'])
def short_link():
    data = request.get_json()
    if not data:
        raise APIException(REQUEST_ERROR)
    if 'url' not in data:
        raise APIException(URL)
    try:
        return jsonify(
            {
                'short_link': url_for(
                    ORIGINAL_LINK_VIEW,
                    short=URLMap.save(
                        short=data.get('custom_id'),
                        original=data['url']
                    ).short,
                    _external=True
                ),
                'url': data.get('url')
            }), HTTPStatus.CREATED
    except Exception as error:
        raise APIException(str(error), HTTPStatus.BAD_REQUEST)


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = URLMap.get(short=short_id)
    if url_map:
        return jsonify({'url': url_map.original}), HTTPStatus.OK
    raise APIException(OBJECT_ERROR, HTTPStatus.NOT_FOUND)
