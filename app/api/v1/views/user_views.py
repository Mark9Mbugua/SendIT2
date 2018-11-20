from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.user_models import User

class UserView(Resource):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    def get(self):
        users = self.usr.logins()

        return make_response(jsonify(
            {
                'Status': "Ok",
                'Message': "Success",
                'Data': users
            }), 200)
    
    #create a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        user_email = data['user_email']
        password = data['password']
        res = self.usr.validate_user_data(user_name, password)
        if res == True:
            resp = self.usr.create(user_name, user_email, password)
            return make_response(jsonify(
                {
                    'Message' : 'Success',
                    'status'  : 'ok',
                    'Data' : resp
                }), 201)
        
        return make_response(jsonify(
            {
                'Message' : res
                
            }), 400)

class SpecificUser(Resource):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    #signin a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        password = data['password']

        if self.usr.userIsValid(user_name) == True:

            res = self.usr.login(user_name, password)

            return res

        return make_response(jsonify(
            {
                'Message': 'User not found'
            }), 404)