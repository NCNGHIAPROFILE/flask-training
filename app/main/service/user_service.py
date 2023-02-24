import uuid
import datetime
import json
from app.main import db
from app.main.model.model import User
from json import JSONEncoder
# class CarJSONEncoder(JSONEncoder):
#     def default(self, obj):
#         return obj.__dict__

def create_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            # password=hash(data['password']),
            password=data['password'],
            name=data['name'],
            birthday=data['birthday'],
            # registered_on=datetime.datetime.utcnow(),
            address=data['address'],
            phone=data['phone'],
            school_id=data['school_id'],
            lesson_id=data['lesson_id'],
            role_id=data['role_id'],
        )
        db.session.add(new_user)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
        # return generate_token(new_user)
    else:
        response_object = {
            'status': '409: Fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def get_all_users():
    user = User.query.all()
    # users = json.dumps(users[0], default=lambda x: x.__dict__)
    # print(json.dumps(User, default=str))
    # for u in user:
    #     u.registered_on = str(u.registered_on)
    # print(type(user[0].registered_on))
    # print(vars(user[0]))

    # users = User.query.with_entities(
    #     User.role_id,
    #     User.lesson_id,
    #     User.updated_on,
    #     User.birthday,
    #     User.email,
    #     User.school_id,
    #     User.password_hash,
    #     User.address,
    #     str(User.registered_on),
    #     User.name,
    #     User.user_id,
    # ).all()
    # users = json.dumps(user, default=str)
    # users = json.loads(users[0])
    return user

def get_a_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    return user

def update_a_user(user_id, data):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        response_object = {
            'status': '409: Fail',
            'message': 'User already exists. Please Again.',
        }
        return response_object, 409
    else:
        user.email = data['email']
        user.password = data['password']
        user.name = data['name']
        user.birthday = data['birthday']
        # user.updated_on = datetime.datetime.utcnow()
        user.address = data['address']
        user.phone = data['phone']
        user.school_id = data['school_id']
        user.lesson_id = data['lesson_id']
        user.role_id = data['role_id']

        db.session.merge(user)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Updated.'
        }
        return response_object, 201

def delete_a_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    db.session.delete(user)
    db.session.commit()

def generate_token(user):
    try:
        auth_token = user.encode_auth_token(user.user_id, user.email, user.name, user.birthday,
                                            user.address, user.phone, user.school_id, user.lesson_id, user.role_id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'JWT-Authorization': auth_token.decode('utf8', 'strict')
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401