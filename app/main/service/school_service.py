import uuid
import datetime

from app.main import db
from app.main.model.model import School


def create_new_schools(data):
    school = School.query.filter_by(school_code=data['code']).first()
    if not school:
        new_school = School(
            school_code=data['code'],
            school_name=data['name'],
            school_address=data['address'],
            school_phone=data['phone'],
            school_boss=data['boss'],
        )
        db.session.add(new_school)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Created.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': '409: Fail',
            'message': 'School already exists. Please Again',
        }
        return response_object, 409


def get_all_schools():
    return School.query.all()

def get_a_schools(school_id):
    return School.query.filter_by(school_id=school_id).first()

def update_a_schools(school_id, data):
    school = School.query.filter_by(school_id=school_id).first()
    if not school:
        response_object = {
            'status': '409: Fail',
            'message': 'School already exists. Please Again.',
        }
        return response_object, 409
    else:
        school.school_code = data['code']
        school.school_name=data['name']
        school.school_address=data['address']
        school.school_phone=data['phone']
        school.school_boss=data['boss']

        db.session.merge(school)
        db.session.commit()
        response_object = {
            'status': '201: Success',
            'message': 'Successfully Updated.'
        }
        return response_object, 201

def delete_a_schools(school_id):
    db.session.delete(School.query.filter_by(school_id=school_id).first())
    db.session.commit()
