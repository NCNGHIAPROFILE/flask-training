from app.main.model.model import User
from ..service.blacklist_service import save_token
import jwt
from app.main.config import Config
from datetime import datetime, timedelta
from flask import jsonify

# is_authenticated: một thuộc tính sẽ được gán là True nếu user có tên và mật mã hợp lệ, False nếu một trong hai không đúng.
# is_active: một thuộc tính được gán là True nếu tài khoản user trong chế độ hoạt động (active) và False nếu ngược lại.
# is_anonymous: một thuộc tính được gán là False cho những user bình thường, và True cho những user ẩn danh (anonymous)
# get_id(): một phương thức để trả về định danh người dùng (id) dưới dạng chuỗi

class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.user_id, user.email, user.name, user.birthday,
                                                    user.address, user.phone, user.school_id, user.lesson_id, user.role_id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'JWT-Authorization': auth_token.decode('utf8', 'strict')
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
        return response_object, 500

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            check = User.decode_auth_token(auth_token)
            if not isinstance(check, str):
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': check
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
    
    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('JWT-Authorization')
        if auth_token:
            check = User.decode_auth_token(auth_token)
            if not isinstance(check, str):
                user = User.query.filter_by(user_id=check).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.user_id,
                        'email': user.email,
                        'Name': user.name,
                        'Birthday': user.birthday,
                        'Address': user.address,
                        'Phone': user.phone,
                        'School_id': user.school_id,
                        'Lesson_id': user.lesson_id,
                        'Role_id': user.role_id,
                        # 'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200

            response_object = {
                'status': 'fail',
                'message': check
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401

    @staticmethod
    def check_role_id(data):
        user = User.query.filter_by(email=data.get('email')).first()
        if user:
            auth_token = user.encode_auth_token(user.user_id, user.email, user.name, user.birthday,
                                                user.address, user.phone, user.school_id, user.lesson_id, user.role_id)
            # auth_token = user.encode_auth_token(user.user_id)
            # auth_token = user.encode_auth_token(user.email)
            if auth_token:
                return user.role_id
        else:
            response_object = {
                'status': '409: Fail',
                'message': 'User already exists. Please Again.',
            }
            return response_object, 409