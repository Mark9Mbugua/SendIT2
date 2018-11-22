from ....db_config import init_db
from flask import jsonify, make_response
from passlib.hash import pbkdf2_sha256 as sha256
import itertools


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
        
    def validate_user_data(self, user_name, password):
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
        return sha256.verify(password, hash)