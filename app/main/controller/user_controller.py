from flask import request, jsonify
import json
from flask_restplus import Api, Resource, fields
from flask_login import login_required
from app.main.service.auth_helper import Auth

from ..util.dto import UserDto, authorizations

from ..util.decorator import token_required
from ..service.user_service import create_new_user, get_all_users, get_a_user, update_a_user, delete_a_user

api = UserDto.api_user
_user = UserDto.user

# 1. api.route : Một trình trang trí để định tuyến tài nguyên
# 2. api.marshal_with : Một trình trang trí chỉ định các trường sẽ sử dụng để tuần tự hóa 
# (Đây là nơi chúng tôi sử dụng chúng userDtotôi đã tạo trước đó)
# 3. api.marshal_list_with : Trình trang trí phím tắt ở marshal_with trên với as_list = True
# 4. api.doc : Trình trang trí để thêm một số tài liệu api vào đối tượng được trang trí
# 5. api.reponse: Một trình trang trí để chỉ định một trong những phản hồi dự kiến
# 6. api.expect: Một trình trang trí để Chỉ định mô hình đầu vào dự kiến
# 7. api.param: Một trình trang trí để chỉ định một trong các tham số dự kiến


# from sqlalchemy.ext.declarative import DeclarativeMeta

# class AlchemyEncoder(json.JSONEncoder):

#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             # an SQLAlchemy class
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     json.dumps(data) # this will fail on non-encodable values, like other classes
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             # a json-encodable dict
#             return fields

#         return json.JSONEncoder.default(self, obj)
@api.route('/') 
class UserList(Resource):
    @api.doc('list_of_registered_users', security='apikey')
    @api.marshal_list_with(_user, envelope='data')
    @token_required
    def get(self):
        """List all registered users"""
        user = get_all_users()
        # return jsonify(user)
        # m = [1,2]
        return user, 200

    @api.response(201, 'User successfully created.')
    @api.response(404, 'User not found.')
    @api.doc(security='apikey')
    @token_required 
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        # pass
        """Creates a new User """
        # print(User.email)
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 5:
            data = request.json
            return create_new_user(data=data), 200
        else:
            api.abort(404) 


@api.route('/<user_id>')
@api.param('user_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    '''Show a single User item and lets you delete them'''
    @api.doc(security='apikey')
    @token_required    
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, user_id):
        """get a user given its identifier"""
        user = get_a_user(user_id)
        if not user:
            api.abort(404)
        else:
            return user, 200

    @api.doc(security='apikey')
    @token_required 
    @api.expect(_user)
    @api.marshal_with(_user)
    def put(self, user_id):
        '''Update a task given its identifier'''
        check = Auth.check_role_id(User.email)
        if check == 5:
            user = get_a_user(user_id)
            if not user:
                api.abort(404)
            else:
                data = request.json
                return update_a_user(user_id, data=data), 200
        else:
            api.abort(404) 

    @api.doc(security='apikey')
    @token_required 
    @api.doc('delete user')
    @api.response(204, 'User deleted')
    def delete(self, user_id):
        '''Delete a task given its identifier'''
        check = Auth.check_role_id(User.email)
        if check == 5:
            delete_a_user(user_id)
            return 'Delete success', 204
        else:
            api.abort(404) 