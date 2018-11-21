from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, 
                                            jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

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

                        }), 201)
            
        else:
            return make_response(jsonify(
                    {
                        'Message' : 'Error in signin up please try again'
                        
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
            access_token = create_access_token(identity = user_name)
            refresh_token = create_refresh_token(identity = password)
                
            return make_response(jsonify({

                    'Message' : 'You are now logged in!',
                    'access_token' : access_token,
                    'refresh_token' : refresh_token,
                    'User' : user
                }), 200)
        
        else:
            return make_response(jsonify({

                        "Message" : 'Enter correct Username or Password'
                    }), 400)
                
            
        

    # def post(self):
    #    data = request.get_json() or {}

    #    if data["email"].find("@") < 2:
    #        message = 'Incorrect email format'
    #        payload = {"Status": "Failed", "Message": message}
    #        return make_response(jsonify(payload), 400)



    #    password = data['password'].strip()
    #    if not (re.match("^[a-zA-Z0-9_]*$", password)):
    #        message = 'Check your password.'
    #        payload = {"Status": "Failed", "Message": message}
    #        return make_response(jsonify(payload), 400)


    #    user = UserModel()
    #    email = data["email"]
    #    password = data["password"]
    #    auth = user.user_login(email)

    #    if auth:
    #        access_token = create_access_token(identity=email)
    #        return make_response(jsonify({"message": "Successful login",
    #        "token": access_token
    #    }), 200)
    #    return make_response(jsonify({
    #    "message": "Try again",
    #    }), 400)