from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, 
                                            jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
from validate_email import validate_email

from ..models.user_models import User

class Register(Resource):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
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
        is_valid=validate_email(email)
        role = data['role']
        password = self.usr.generate_hash(data['password'])
        res = self.usr.validate_user_data(user_name, password)
        if res == True:
                resp = self.usr.register(user_name, email, role, password)
                if resp == True:
                    return make_response(jsonify(
                        {
                            'Message' : 'Signed up successfully',
                            'status'  : 'ok',
                            'Data' : resp

                        }), 201)
            
        else:
            return make_response(jsonify(
                    {
                        'Message' : 'Error in sign up. please try again'
                        
                    }), 400)

class Login(Resource):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    # sign in a user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name', help = "Required", required=True)
        parser.add_argument('password', help = "Required", required=True)
        data = parser.parse_args()
        user_name = data['user_name']
        password = data['password']

        if self.usr.userIsValid(user_name) == True:
            user = self.usr.login(user_name, password)
            access_token = create_access_token(identity = user)
            refresh_token = create_refresh_token(identity = user)
                
            return make_response(jsonify({

                    'Message' : 'You are now logged in!',
                    'access_token' : access_token,
                    'refresh_token' : refresh_token
                }), 200)
        
        else:
            return make_response(jsonify({

                        "Message" : 'Enter correct Username or Password'
                    }), 400)