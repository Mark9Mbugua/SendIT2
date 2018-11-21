import unittest
import os
import json
from app import make_app
class TestParcel(unittest.TestCase):
    def setUp(self):
        app = make_app(config_name="testing")
        self.client = app.test_client()
        self.data = {
            "parcel_name" 	: "Leather Sofa Set",
            "parcel_weight": "150kg",
            "pick_location": "Survey",
            "destination" 	: "Wendani",
            "consignee_name": "Mark Mbugua",
            "consignee_no" 	: "0712340908",
            "order_status": "order_status",
            "user_id": 1
		}	
    def test_post_parcel(self):
	    res = self.client.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
	    result = json.loads(res.data)
	    self.assertEqual(result['Response'], "Parcel Created")
	    self.assertEqual(res.status_code, 201)
    
    def test_get_all_parcels(self):
        res = self.client.get('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        result = json.loads(res.data)
        self.assertEqual(result['Response'], "Parcels Ready")
        self.assertEqual(res.status_code, 200)
 	
    def test_get_parcel(self):
        rv = self.client.post('/api/v1/parcels',data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        result = self.client.get('/api/v1/parcels/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Leather Sofa', str(result.data))
	
    def test_get_parcel_invalid_id(self):
        rv = self.client.post('/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        result = self.client.get('/api/v1/parcels/106')
        self.assertEqual(result.status_code, 400)
	
    def test_cancel_parcel(self):
        rv = self.client.post('/api/v1/parcels',data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        result = self.client.put('/api/v1/parcels/1/cancel')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Cancelled', str(result.data))
	
    def test_cancel_parcel_invalid_id(self):
        rv = self.client.post('/api/v1/parcels',data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        result = self.client.put('/api/v1/parcels/106/cancel')
        self.assertEqual(result.status_code, 404)

    def test_user_parcels(self):
        rv = self.client.post('/api/v1/parcels',data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(rv.status_code, 201)
        result = self.client.get('/api/v1/users/1/parcels')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Leather Sofa', str(result.data))
        
if __name__ == '__main__':
	unittest.main() 
