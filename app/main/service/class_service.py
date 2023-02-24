import uuid
import datetime

from app.main import db
from app.main.model.model import Class, Lesson, Subject

# class
def create_new_class(data):
    classs = Class.query.filter_by(class_name=data['name']).first()
    if not classs:
        new_classs = Class(
            class_name=data['name'],
            class_detail=data['detail'],
            school_id=data['school_id'],
        )
        db.session.add(new_classs)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': '409: Fail',
            'message': 'Class already exists. Please Again',
        }
        return response_object, 409

def get_all_class():
    return Class.query.all()

def get_a_class(class_id):
    return Class.query.filter_by(class_id=class_id).first()

def update_a_class(class_id, data):
    classs = Class.query.filter_by(class_id=class_id).first()
    if not classs:
        response_object = {
            'status': '409: Fail',
            'message': 'Class already exists. Please Again.',
        }
        return response_object, 409
    else:
        classs.class_name=data['name'],
        classs.class_detail=data['detail']
        classs.school_id=data['school_id']
        db.session.merge(classs)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Updated.'
        }
        return response_object, 201

def delete_a_class(class_id):
    db.session.delete(Class.query.filter_by(class_id=class_id).first())
    db.session.commit()
# ---------------------------------------------

# lesson
def create_new_lessons(data):
    lessons = Lesson.query.filter_by(lesson_name=data['name']).first()
    if not lessons:
        new_lessons = Lesson(
            lesson_name=data['name'],
            lesson_detail=data['detail'],
        )
        db.session.add(new_lessons)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': '409: Fail',
            'message': 'Lesson already exists. Please Again',
        }
        return response_object, 409

def get_all_lessons():
    return Lesson.query.all()

def get_a_lessons(lesson_id):
    return Lesson.query.filter_by(lesson_id=lesson_id).first()

def update_a_lessons(lesson_id, data):
    lessons = Lesson.query.filter_by(lesson_id=lesson_id).first()
    if not lessons:
        response_object = {
            'status': '409: Fail',
            'message': 'Lesson already exists. Please Again.',
        }
        return response_object, 409
    else:
        lessons.lesson_name=data['name'],
        lessons.lesson_detail=data['detail']
        db.session.merge(lessons)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Updated.'
        }
        return response_object, 201

def delete_a_lessons(lesson_id):
    db.session.delete(Lesson.query.filter_by(lesson_id=lesson_id).first())
    db.session.commit()
# ---------------------------------------------

# subject
def create_new_subjects(data):
    subjects = Subject.query.filter_by(subject_name=data['name']).first()
    if not subjects:
        new_subjects = Subject(
            subject_name=data['name'],
            subject_detail=data['detail'],
            class_id=data['class_id'],
        )
        db.session.add(new_subjects)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': '409: Fail',
            'message': 'Subject already exists. Please Again',
        }
        return response_object, 409

def get_all_subjects():
    return Subject.query.all()

def get_a_subjects(subject_id):
    return Subject.query.filter_by(subject_id=subject_id).first()

def update_a_subjects(subject_id, data):
    subjects = Subject.query.filter_by(subject_id=subject_id).first()
    if not subjects:
        response_object = {
            'status': '409: Fail',
            'message': 'Subject already exists. Please Again.',
        }
        return response_object, 409
    else:
        subjects.subject_name=data['name'],
        subjects.subject_detail=data['detail']
        subjects.class_id=data['class_id']
        
        db.session.merge(subjects)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Updated.'
        }
        return response_object, 201

def delete_a_subjects(subject_id):
    db.session.delete(Subject.query.filter_by(subject_id=subject_id).first())
    db.session.commit()

