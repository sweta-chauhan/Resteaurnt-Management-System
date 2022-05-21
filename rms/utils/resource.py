from functools import wraps
import flask_restful as restful
from datetime import datetime
from decimal import Decimal
import traceback

from flask import current_app as app


def is_2XX(code):
    return code / 100 == 2


def sanitize_date(data):
    if isinstance(data, list):
        data = [sanitize_date(x) for x in data]
    elif isinstance(data, dict):
        data = python_dict_to_json(data)
    return data


def format_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, http_status, headers = sanitize_response(func(*args, **kwargs))
        return data, http_status, headers

    return wrapper


def handle_redirects(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, http_status, headers = sanitize_response(func(*args, **kwargs))
        if http_status in [301, 302]:
            return redirect(data, code=http_status)
        else:
            return data, http_status, headers

    return wrapper


def python_dict_to_json(data):
    for k, v in data.items():
        if isinstance(v, datetime):
            data[k] = datetime.strftime(v, "%Y-%m-%dT%H:%M:%SZ")

        elif isinstance(v, Decimal):
            data[k] = float(v)
        else:
            data[k] = sanitize_date(v)
    return data


def sanitize_response(response):
    http_status = 200
    headers = {}
    if isinstance(response, tuple):
        (data, http_status, headers) = response
    else:
        data = response
    data = sanitize_date(data)
    if is_2XX(http_status) and isinstance(data, list):
        data = dict(
            results=data,
            count=len(data),
            hasPrev=False,
            hasNext=False
        )

    return data, http_status, headers


def format_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data, http_status, headers = sanitize_response(func(*args, **kwargs))
        return data, http_status, headers

    return wrapper


def cors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            data, status, headers = func(*args, **kwargs)

            cors_allow_headers = ', '.join(app.config.get('CORS_ALLOW_HEADERS',
                                                          ["*", "authorization", "client-code", 'Content-Type',
                                                           'Client-Code', 'Accept-Language', 'Authorization']))
            cors_allow_origins = ', '.join(app.config.get('CORS_ALLOW_ORIGINS', ["*"]))
            cors_allow_methods = ', '.join(app.config.get('CORS_ALLOW_METHODS', ["*"]))

            headers.update({
                'Access-Control-Allow-Headers': cors_allow_headers,
                'Access-Control-Allow-Origin': cors_allow_origins,
                'Access-Control-Allow-Methods': cors_allow_methods
            })
            return data, status, headers

        except Exception as e:
            traceback.print_exc()

    return wrapper


class BaseResource(restful.Resource):
    method_decorators = [format_response, cors, handle_redirects]

    def options(self, *args, **kwargs):
        return {"status": "OPTIONS OK"}
