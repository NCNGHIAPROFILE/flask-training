from flask import request
from flask_restplus import Api, Resource, fields

from ..util.dto import ClassDto, LessonDto, SubjectDto
from ..util.decorator import token_required
from app.main.service.auth_helper import Auth
from app.main.model.model import User

from ..service.class_service import get_all_class, get_a_class, update_a_class, create_new_class, delete_a_class
from ..service.class_service import get_all_subjects, get_a_subjects, update_a_subjects, create_new_subjects , delete_a_subjects
from ..service.class_service import get_all_lessons, get_a_lessons, update_a_lessons, create_new_lessons, delete_a_lessons


api_class = ClassDto.api_class
_class = ClassDto.classes

api_lesson = LessonDto.api_lesson
_lesson = LessonDto.lesson

api_subject = SubjectDto.api_subject
_subject = SubjectDto.subject

# class
@api_class.route('/') 
class ClassList(Resource):
    @api_class.doc('list_of_registered_classes', security='apikey')
    @token_required
    @api_class.marshal_list_with(_class, envelope='data')
    def get(self):
        """List all registered classes"""
        return get_all_class()

    @api_class.response(201, 'Class successfully created.')
    @api_class.doc('create a new Class', security='apikey')
    @token_required
    @api_class.expect(_class, validate=True)
    def post(self):
        """Creates a new Class """
        check = Auth.check_role_id(User.email)
        print (check)
        if check >= 3:
            data = request.json
            return create_new_class(data=data)
        else:
            api_class.abort(404) 


@api_class.route('/<class_id>')
@api_class.param('class_id', 'The Class identifier')
@api_class.response(404, 'Class not found.')
class Class(Resource):
    '''Show a single Class item and lets you delete them'''

    @api_class.doc('get a Class', security='apikey')
    @token_required
    @api_class.marshal_with(_class)
    def get(self, class_id):
        """get a class given its identifier"""
        classs = get_a_class(class_id)
        if not classs:
            api_class.abort(404)
        else:
            return classs

    @api_class.expect(_class)
    @api_class.marshal_with(_class)
    @api_class.doc(security='apikey')
    @token_required
    def put(self, class_id):
        '''Update a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 3 or check == 4:
            classs = get_a_class(class_id)
            if not classs:
                api_class.abort(404)
            else:
                data = request.json
                return update_a_class(class_id, data=data), 200
        else:
            api_class.abort(404) 

    @api_class.doc('delete class', security='apikey')
    @token_required
    @api_class.response(204, 'Class deleted')
    def delete(self, class_id):
        '''Delete a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 3 or check == 4:
            delete_a_class(class_id)
            return 'Delete success', 204
        else:
            api_class.abort(404) 

# -------------------------------------------

# Lesson
@api_lesson.route('/') 
class LessonList(Resource):
    @api_lesson.doc('list_of_registered_lessons', security='apikey')
    @token_required
    @api_lesson.marshal_list_with(_lesson, envelope='data')
    def get(self):
        """List all registered lessons"""
        return get_all_lessons()

    @api_lesson.response(201, 'Lesson successfully created.')
    @api_lesson.doc('create a new Lesson', security='apikey')
    @token_required
    @api_lesson.expect(_lesson, validate=True)
    def post(self):
        """Creates a new Lesson """
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            data = request.json
            return create_new_lessons(data=data), 200
        else:
            api_class.abort(404) 


@api_lesson.route('/<lesson_id>')
@api_lesson.param('lesson_id', 'The Lesson identifier')
@api_lesson.response(404, 'Lesson not found.')
class Lesson(Resource):
    '''Show a single Lesson item and lets you delete them'''

    @api_lesson.doc('get a Lesson', security='apikey')
    @token_required
    @api_lesson.marshal_with(_lesson)
    def get(self, lesson_id):
        """get a lesson given its identifier"""
        lesson = get_a_lessons(lesson_id)
        if not lesson:
            api_lesson.abort(404)
        else:
            return lesson

    @api_lesson.expect(_lesson)
    @api_lesson.marshal_with(_lesson)
    @api_lesson.doc(security='apikey')
    @token_required
    def put(self, lesson_id):
        '''Update a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            lesson = get_a_lessons(lesson_id)
            if not lesson:
                api_lesson.abort(404)
            else:
                data = request.json
                return update_a_lessons(lesson_id, data=data), 200
        else:
            api_class.abort(404) 

    @api_lesson.doc('delete lesson', security='apikey')
    @token_required
    @api_lesson.response(204, 'Lesson deleted')
    def delete(self, lesson_id):
        '''Delete a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            delete_a_lessons(lesson_id)
            return 'Delete success', 204
        else:
            api_class.abort(404) 
# -------------------------------------------

# subject
@api_subject.route('/') 
class SubjectList(Resource):
    @api_subject.doc('list_of_registered_subjects', security='apikey')
    @token_required
    @api_subject.marshal_list_with(_subject, envelope='data')
    def get(self):
        """List all registered subject"""
        return get_all_subjects()

    @api_subject.response(201, 'Subject successfully created.')
    @api_subject.doc('create a new Subject', security='apikey')
    @token_required
    @api_subject.expect(_subject, validate=True)
    def post(self):
        """Creates a new Subject """
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            data = request.json
            return create_new_subjects(data=data), 200
        else:
            api_class.abort(404) 


@api_subject.route('/<subject_id>')
@api_subject.param('subject_id', 'The Subject identifier')
@api_subject.response(404, 'Subject not found.')
class Subject(Resource):
    '''Show a single Subject item and lets you delete them'''

    @api_subject.doc('get a Subject', security='apikey')
    @token_required
    @api_subject.marshal_with(_subject)
    def get(self, subject_id):
        """get a subject given its identifier"""
        subject = get_a_subjects(subject_id)
        if not subject:
            api_subject.abort(404)
        else:
            return subject

    @api_subject.expect(_subject)
    @api_subject.marshal_with(_subject)
    @api_subject.doc(security='apikey')
    @token_required
    def put(self, subject_id):
        '''Update a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            subject = get_a_subjects(subject_id)
            if not subject:
                api_subject.abort(404)
            else:
                data = request.json
                return update_a_subjects(subject_id, data=data), 200
        else:
            api_class.abort(404) 

    @api_subject.doc('delete subject', security='apikey')
    @token_required
    @api_subject.response(204, 'Subject deleted')
    def delete(self, subject_id):
        '''Delete a task given its identifier'''
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 2 or check == 3 or check == 4:
            delete_a_subjects(subject_id)
            return 'Delete success', 204
        else:
            api_class.abort(404) 

# -------------------------------------------

