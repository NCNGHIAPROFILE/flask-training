from flask import request
from flask_restplus import Resource
from ..util.decorator import token_required
from app.main.model.model import User

from ..util.dto import SchoolDto
from ..service.school_service import get_all_schools, get_a_schools, update_a_schools, delete_a_schools, create_new_schools
from ..util.decorator import token_required
from app.main.service.auth_helper import Auth



api = SchoolDto.api_school
_school = SchoolDto.school

@api.route('/')
class SchoolList(Resource):
    @api.doc('list_of_registered_schools', security='apikey')
    @token_required
    @api.marshal_list_with(_school, envelope='data')
    def get(self):
        """List all registered schools"""
        return get_all_schools(), 200

    @api.response(201, 'School successfully created.')
    @api.doc('create a new School', security='apikey')
    @token_required
    @api.expect(_school, validate=True)
    def post(self):
        """Creates a new Schools"""
        check = Auth.check_role_id(User.email)
        print (check)
        if check == 5:
            data = request.json
            return create_new_schools(data=data)
        else:
            api.abort(404) 


@api.route('/<school_id>')
@api.param('school_id', 'The School identifier')
@api.response(404, 'School not found.')
class School(Resource):
    '''Show a single School item and lets you delete them'''

    @api.doc('get a school', security='apikey')
    @token_required
    @api.marshal_with(_school)
    def get(self, school_id):
        """get a school given its identifier"""
        school = get_a_schools(school_id)
        if not school:
            api.abort(404)
        else:
            return school, 200

    @api.expect(_school)
    @api.marshal_with(_school)
    @api.doc(security='apikey')
    @token_required
    def put(self, school_id):
        '''Update a task given its identifier'''
        check = Auth.check_role_id(User.email)
        if check == 3 or check == 4:
            school = get_a_schools(school_id)
            if not school:
                api.abort(404)
            else:
                data = request.json
                return update_a_schools(school_id, data=data), 200
        else:
            api.abort(404) 

    @api.doc('delete shcool', security='apikey')
    @token_required
    @api.response(204, 'School deleted')
    def delete(self, school_id):
        '''Delete a task given its identifier'''
        check = Auth.check_role_id(User.email)
        if check == 3 or check == 4:
            delete_a_schools(school_id)
            return 'Delete success', 204
        else:
            api.abort(404) 