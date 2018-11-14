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

	        
    def tearDown(self):
        pass
	

if __name__ == '__main__':
	unittest.main()