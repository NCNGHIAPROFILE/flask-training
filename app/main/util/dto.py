from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    }
}

class UserDto:
    # tạo một không gian tên mới cho các hoạt động liên quan đến người dùng. Flask-RESTPlus cung cấp cách sử dụng
    # gần như cùng một mẫu với Blueprint . Ý tưởng chính là chia ứng dụng của bạn thành các không gian tên có thể tái sử dụng. 
    # Một mô-đun không gian tên sẽ chứa các mô hình và khai báo tài nguyên.
    api_user = Namespace('user', description='user related operations', authorizations=authorizations)
    user = api_user.model('user', {
        'email': fields.String(required=True, description='user email'),
        'password': fields.String(required=True, description='user password'),
        'name': fields.String(required=True, description='user name'),
        'birthday': fields.String(required=True, description='user birthday'),
        'address': fields.String(required=True, description='user address'),
        'phone': fields.String(required=True, description='user phone'),
        'school_id': fields.Integer(required=True, description='school name'),
        'lesson_id': fields.Integer(required=True, description='lesson name'),
        'role_id': fields.Integer(required=True, description='user role'),
    })


class SchoolDto:
    api_school = Namespace('school', description='school related operations')
    school = api_school.model('school', {
        'code': fields.String(required=True, description='school code'),
        'name': fields.String(required=True, description='school name'),
        'address': fields.String(required=True, description='school address'),
        'phone': fields.String(required=True, description='school phone'),
        'boss': fields.String(required=True, description='school boss')
    })


class RoleDto:
    api_role = Namespace('role', description='role related operations')
    role = api_role.model('role', {
        'name': fields.String(required=True, description='role position'),
    })


class ClassDto:
    api_class = Namespace('class', description='class related operations')
    classes = api_class.model('class', {
        'name': fields.String(required=True, description='class name'),
        'detail': fields.String(required=True, description='class detail'),
        'school_id': fields.Integer(required=True, description='school name')
    })


class SubjectDto:
    api_subject = Namespace('subject', description='subject related operations')
    subject = api_subject.model('subject', {
        'name': fields.String(required=True, description='subject name'),
        'detail': fields.String(required=True, description='subject detail'),
        'class_id': fields.Integer(required=True, description='class name')
    })

    
class LessonDto:
    api_lesson = Namespace('lesson', description='lesson related operations')
    lesson = api_lesson.model('lesson', {
        'name': fields.String(required=True, description='lesson name'),
        'detail': fields.String(required=True, description='lesson detail')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })