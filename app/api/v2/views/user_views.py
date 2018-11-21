from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request

from ..models.user_models import User

class UserView(Resource):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    # signup a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        email = data['email']
        role = data['role']
        password = data['password']
        res = self.usr.validate_user_data(user_name, password)
        if res == True:
            resp = self.usr.register(user_name, email, role, password)
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
    
    # sign in a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        password = data['password']

        if self.usr.userIsValid(user_name) == True:

            user = self.usr.login(user_name, password)

            return make_response(jsonify({

                "Message" : 'You are now logged in!',
                "Data" : user
            }), 200)
            
        return make_response(jsonify({

            "Message" : 'Enter correct Username or Password'
        }), 400)
        