from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.school_controller import api as school_ns
from .main.controller.class_controller import api_class as class_ns, api_lesson as lesson_ns, api_subject as subject_ns
from .main.controller.auth_controller import api as auth_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API WITH NGHIANC',
          version='1.0',
          description='flask restplus web service CRUD'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(school_ns, path='/school')
api.add_namespace(class_ns, path='/class')
api.add_namespace(lesson_ns, path='/lesson')
api.add_namespace(subject_ns, path='/subject')
api.add_namespace(auth_ns)

