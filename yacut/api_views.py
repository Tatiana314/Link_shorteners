from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app
from .constants import OBJECT_ERROE
from .error_handlers import APIException
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def short_link():
    url_map = URLMap.validate_on_save(request.get_json())
    return jsonify(
        {
            'short_link': url_for(
                'original_link_view',
                short=url_map.short,
                _external=True
            ),
            'url': url_map.original
        }), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original_link = URLMap.query.filter_by(short=short_id).first()
    if original_link:
        return jsonify({'url': original_link.original}), HTTPStatus.OK
    raise APIException(OBJECT_ERROE, HTTPStatus.NOT_FOUND)
