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
        return self.users
        
        #get one user
    def getuser(self, user_name, password):
        for detail in self.users:

            if detail['user_name'] == user_name:

                if detail['password'] == password:

                    return make_response(jsonify(
                        {
                            'Message': "User is now logged in!"
                        }), 200)

            return make_response(jsonify(
                {
                    'Message': "Enter correct Username and Password"
                }), 400)

    def userisvalid(self, user_name):

        for user in self.users:
            if(user['user_name'] == user_name):
                return True
    
    def validate_data(self, user_name, password):
        try:
            if len(user_name) < 3:
                return "username must be more than 3 characters"
            elif len(password) < 5:
                return "Password should be at least 5 characters"
            elif " " in password:
                return "Password should be one word, no spaces"
            else:
                return True

        except Exception as error:
            return make_response(jsonify(
                {
                    'Message': "Username or Password dont meet starndards" +str(error)
                }), 401)