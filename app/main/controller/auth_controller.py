from flask import request
from flask_restplus import Resource
from flask_login import login_required
from ..util.dto import authorizations
from ..util.decorator import token_required


from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc(security='apikey')
    @token_required
    @api.doc('logout a user')
    def post(self):
        auth_header = request.headers.get('JWT-Authorization')
        return Auth.logout_user(data=auth_header)