from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.user_models import User

class UserView(Resource, User):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    def get(self):
        users = self.usr.getusers()

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
        res = self.usr.validate_data(user_name, password)
        if res == True:
            resp = self.usr.hold(user_name, user_email, password)
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

class SpecificUser(Resource, User):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    #signin a user
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        password = data['password']

        if self.usr.userisvalid(user_name) == True:

            res = self.usr.getuser(user_name, password)

            return res

        return make_response(jsonify(
            {
                'Message': 'User not found'
            }), 401)


        
    

