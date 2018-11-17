import unittest
import os
import json
from app import make_app

class TestUser(unittest.TestCase):
    
    def setUp(self):
        app = make_app(config_name="testing")
        self.client = app.test_client()
        self.data = {
            'user_name' : "Markman",
            'user_email'  :  "mbugua@gmail.com",
            'password' :    "markman"
        }
    def test_user_login(self):
        #sign user up first
        rv = self.client.post('/api/v1/signup', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)

        #check user can login
        result = self.client.post('/api/v1/login', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(result.status_code, 200)


    def test_user_signup(self):
        res = self.client.post('/api/v1/signup', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result['Message'], "Success")
        self.assertEqual(res.status_code, 201)
    
    def test_signup_user_shortusername(self):
        res = self.client.post('/api/v1/signup', data=json.dumps({'user_name' : "ma", 'password' : "markmain", "user_email" : 'mbuguamark@gmail.com'}), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result["Message"], "username must be more than 3 characters")
        self.assertEqual(res.status_code, 400)

    def test_signup_user_sparcele_password(self):
        res = self.client.post('/api/v1/signup', data=json.dumps({'user_name' : "marky", 'password' : "markma ", "user_email" : 'mbuguamark@gmail.com'}), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result["Message"], "Password should be one word, no sparceles")
        self.assertEqual(res.status_code, 400)
    
    def test_signup_user_short_password(self):
        res = self.client.post('/api/v1/signup', data=json.dumps({'user_name' : "marky", 'password' : "mark", "user_email" : 'mbuguamark@gmail.com'}), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result["Message"], "Password should be at least 5 characters")
        self.assertEqual(res.status_code, 400)
	        
    def tearDown(self):
        pass
	

if __name__ == '__main__':
	unittest.main()