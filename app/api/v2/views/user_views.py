from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, 
                                            jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from ..models.user_models import User

class Register(Resource):
    
    # initialize the user class
    def __init__(self):
        self.user = User()
    
    # signup a user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', help = "Required", required=True)
        parser.add_argument('password', help = "Required", required=True)
        parser.add_argument('email', help = "Required", required=True)
        parser.add_argument('role', help = "Required", required=True)

        data = parser.parse_args()
        user_name = data['user_name']
        email = data['email']
        role = data['role']
        password = self.user.generate_hash(data['password'])
        res = self.user.validate_user_data(user_name, password)
        if res == True:
                resp = self.user.register(user_name, email, role, password)
                return make_response(jsonify(
                    {
                        'Message' : 'User signed up successfully',
                        'status'  : 'ok',
                        'Data' : resp

                    }), 201)
        
        return make_response(jsonify(
                {
                    'Message' : 'Kindly check if username or password is correct and in the required format'
                    
                }), 400)

class Login(Resource):
    
    # initialize the user class
    def __init__(self):
        self.user = User()
    
    # sign in a user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', help = "Required", required=True)
        parser.add_argument('password', help = "Required", required=True)
        data = parser.parse_args()
        user_name = data['user_name']
        password = data['password']

        if self.user.userIsValid(user_name) == True:
            user = self.user.login(user_name, password)
            access_token = create_access_token(identity = user)
                
            return make_response(jsonify({

                    'Message' : 'You are now logged in!',
                    'access_token' : access_token

                }), 200)
        
        else:
            return make_response(jsonify({

                        "Message" : 'Enter correct Username or Password'
                    }), 400)