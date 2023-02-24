from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key
# Mỗi khi mô hình cơ sở dữ liệu thay đổi, hãy lặp lại các lệnh 
# migrate: python manage.py db migrate
# và upgrade: python manage.py db upgrade

class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=True)
    birthday = db.Column(db.String(10), nullable=True)
    # registered_on = db.Column(db.DateTime, nullable=True)
    # updated_on = db.Column(db.DateTime, nullable=True)
    address = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(11), nullable=True)
    school_id = db.Column(db.Integer, nullable=False)
    # db.ForeignKey('school.school_id'), 
    lesson_id = db.Column(db.Integer, nullable=False)
    # db.ForeignKey('lesson.lesson_id')
    role_id = db.Column(db.Integer, nullable=False)
    # db.ForeignKey('role.role_id'),
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf8', 'strict')
        # là một trình thiết lập cho trường password_hashvà nó sử dụng flask-bcryptđể tạo hàm băm bằng mật khẩu được cung cấp.

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
        # so sánh mật khẩu đã cho với mật khẩu đã lưu password_hash.

    def __repr__(self):
        return '<User {}>'.format(self.email) 

    def encode_auth_token(self, user_id, email, name, birthday,
                        address, phone, school_id, lesson_id, role_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'User_id': user_id,
                'Email': email,
                'Name': name,
                'Birthday': birthday,
                # 'Register_on': str(registered_on),
                'Address': address,
                'Phone': phone,
                'School_id': school_id,
                'Lesson_id': lesson_id,
                'Role_id': role_id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow()
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod  
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['User_id', 'Email', 'Name', 'Birthday', 'Address', 'Phone', 'School_id', 'Lesson_id', 'Role_id']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class School(db.Model):
    """ School Model for storing user related details """
    __tablename__ = "school"

    school_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school_code = db.Column(db.String(100), unique=True, nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    school_address = db.Column(db.String(100), nullable=True)
    school_phone = db.Column(db.String(11), nullable=True)
    school_boss = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<School {}>'.format(self.school_name) 

class Class(db.Model):
    """ Class Model for storing user related details """
    __tablename__ = "class"

    class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(100), unique=True, nullable=False)
    class_detail = db.Column(db.String(150), nullable=True)
    school_id = db.Column(db.Integer, nullable=False)
    # , db.ForeignKey('school.school_id')

    def __repr__(self):
        return '<Class {}>'.format(self.class_name) 

class Role(db.Model):
    """ Role Model for storing user related details """
    __tablename__ = "role"

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_position = db.Column(db.String(100), unique=True, nullable=False)


class Lesson(db.Model):
    """ Lesson Model for storing user related details """
    __tablename__ = "lesson"

    lesson_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lesson_name = db.Column(db.String(100), unique=True, nullable=False)
    lesson_detail = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return '<Lesson {}>'.format(self.lesson_name) 

class Subject(db.Model):
    """ Subject Model for storing user related details """
    __tablename__ = "subject"

    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.String(100), unique=True, nullable=False)
    subject_detail = db.Column(db.String(150), nullable=True)
    class_id = db.Column(db.Integer, nullable=False)
    # , db.ForeignKey('class.class_id')

    def __repr__(self):
        return '<Subject {}>'.format(self.subject_name) 