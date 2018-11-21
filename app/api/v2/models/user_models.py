from ....db_config import init_db
from flask import jsonify, make_response
from passlib.hash import pbkdf2_sha256 as sha256


class User():

    def __init__(self):
        self.db = init_db()
    
    def serializer(self, user):
        user_fields = ('user_name', 'email', 'role', 'password')
        result = dict()
        for index, field in enumerate(user_fields):
            result[field] = user[index]
        return result
    
    def register(self, user_name, email, role, password):
        cur = self.db.cursor()
        query = """INSERT INTO users (user_name, email, role, password)
                VALUES (%s, %s, %s, %s)"""
        content = (user_name, email, role, password)
        cur.execute(query, content)
        self.db.commit()
        self.db.close()
        return self.serializer(content)


    def login(self, user_name, password):
        cur = self.db.cursor()
        cur.execute("""SELECT user_name, email, role, password FROM users WHERE user_name = %s and password = %s""", (user_name, password))
        db_user = cur.fetchone()
        return self.serializer(db_user)

    def userIsValid(self, user_name):
        cur = self.db.cursor()
        cur.execute("""SELECT user_name, email, role, password FROM users WHERE user_name = %s""", (user_name, ))
        data = cur.fetchall()
        for user in data:
            if user[0] == user_name:
                return True
        
    def validate_user_data(self, user_name, password):
        try:
            if len(user_name) < 3:
                return "username must be more than 3 characters"
            elif len(password) < 5:
                return "Password should be at least 5 characters"
            elif " " in password:
                return "Password should be one word, no sparceles"
            else:
                return True

        except Exception as error:
            return make_response(jsonify(
                {
                    'Message': "Username or Password dont meet starndards" +str(error)
                }), 401)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)