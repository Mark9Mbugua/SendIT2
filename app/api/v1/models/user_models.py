from flask import jsonify, make_response

# make a user list available to a class
# list we are going to use to store user details
users = []

class User():
    def __init__(self):
        
        self.users = users

    def hold(self, user_name, user_email, password):
        userdetails = {
            'user_id' : len(self.users) + 1,
            'user_name' : user_name,
            'user_email' : user_email,
            'password' : password
        }

        self.users.append(userdetails)
        return self.users

    #get all users
    def getusers(self):
        pass
        
        #get one user
    def getuser(self, user_name, password):
        pass

    def userexists(self, user_name):
        pass