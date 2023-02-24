from functools import wraps
from flask import request

from app.main.service.auth_helper import Auth
from app.main.config import Config
from app.main.util.dto import authorizations

# https://paste.ofcode.org/PTApETjwyYvEzaSxjyZFCz

# chỉ cần thêm quyền cho API bằng cách thêm @api.doc(security='apikey') và @token_required ở đầu phương thức API
# https://aaronluna.dev/series/flask-api-tutorial/part-4/
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print(request.headers)
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return {'message' : 'Token is missing'}, 401

        return f(*args, **kwargs)
    return decorated