from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.user_models import User

class Register(Resource):
    
    # initialize the user class
    def __init__(self):
        self.user = User()
    
    def get(self):
        users = self.user.logins()

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
        email = data['email']
        password = data['password']
        res = self.user.validate_user_data(user_name, password)
        if res == True:
            resp = self.user.create(user_name, email, password)
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

class Login(Resource):
    
    # initialize the user class
    def __init__(self):
        self.user = User()
    
    #signin a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        password = data['password']

        if self.user.userIsValid(user_name) == True:

            res = self.user.login(user_name, password)

            return res

        return make_response(jsonify(
            {
                'Message': 'User not found'
            }), 404)