from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.user_models import User

class UserView(Resource, User):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    #create a user
    def post(self):
        pass

    
    def get(self):
        pass
    
class SpecificUser(Resource, User):
    
    # initialize the user class
    def __init__(self):
        self.usr = User()
    
    #signin a user
    def post(self):
        pass

        
    
