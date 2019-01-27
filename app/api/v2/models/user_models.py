from ....db_config import init_db
from flask import jsonify, make_response
from passlib.hash import pbkdf2_sha256 as sha256
import itertools
import re


class User():

    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        user_fields = ('user_id', 'user_name', 'email', 'role', 'password')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def second_serializer(self, user_details):
        user_id, user_name, email, role, password = user_details
        result = dict(user_id = user_id, user_name = user_name, email = email, role = role, password = password)

        return result
    
    def third_serializer(self, password):
        (pwd ,) = password
        result = dict(pwd=pwd)

        return result

    
    def register(self, user_name, email, role, password):
        cur = self.db.cursor()
        query = """INSERT INTO users (user_name, email, role, password)
                VALUES (%s, %s, %s, %s) RETURNING user_id"""
        content = (user_name, email, role, password)
        cur.execute(query, content)
        user_id = cur.fetchone()
        self.db.commit()
        self.db.close()
        output = self.serializer(tuple(itertools.chain(user_id, content)))
        return output

    def login(self, user_name, password):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, user_name, email, role, password FROM users WHERE user_name = %s""", (user_name, ))
        user= cur.fetchone()
        if cur.rowcount == 1: 
            data = self.serializer(user)
            if self.verify_hash(password, data["password"]) is True:  
                return data

    def userIsValid(self, user_name):
        cur = self.db.cursor()
        cur.execute("""SELECT user_id, user_name, email, role, password FROM users WHERE user_name = %s""", (user_name, ))
        data = cur.fetchall()
        for user in data:
            if user[1] == user_name:
                return True
    
    def password_is_valid(self, user_name, password):
        """Check if password is correct"""
        cur = self.db.cursor()
        cur.execute("""SELECT password FROM users WHERE user_name = %s""", (user_name, ))
        data = cur.fetchone()
        passcode = self.third_serializer(data)
        if self.verify_hash(password, passcode["pwd"]) is  True:
            return True
            


    def validate_user_data(self, user_name, password):
        """validates user data"""
        response  = True
        if len(user_name) < 4:
            response = "username should have at least 3 characters"
            return response

        elif len(password) < 5:
            response = "Password should have at least 5 characters"
            return response
        
        elif " " in password:
            response = "Password should be one word, no spaces"
            return response

        elif not re.search('[A-Z]', password):
            response = "Password should have at least one capital letter"
            return response

        elif not re.search('[a-z]', password):
            response = "Password should have at least one lowercase letter"
            return response 
        
        elif not re.search('[0-9]', password):
            response =  "Password should have at least one number"
            return response

        return response
    
    
    def getOneUser(self, user_id):
        cur = self.db.cursor() 
        cur.execute("""SELECT user_id, user_name, email, role, password FROM users WHERE user_id = '{}'""" .format(user_id))
        data = cur.fetchone()
        return self.second_serializer(data)

    def getUserName(self, user_name):
        cur = self.db.cursor() 
        query = """SELECT  user_id, user_name, email, role, password FROM users WHERE user_name = '{}';""".format(user_name)
        cur.execute(query)
        data = cur.fetchone()
        user_dict = {data[0]: [data[1], data[2], data[3], data[4]],}
        return user_dict

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        """returns True if password has been hashed"""
        return sha256.verify(password, hash)