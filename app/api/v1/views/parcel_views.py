from flask_restful import Resource
from flask import jsonify, make_response, request, sessions

from ..models.parcel_models import Parcel


class ParcelView(Resource, Parcel):
   

    def __init__(self):
        self.pac = Parcel()

    def post(self):
        data = request.get_json()
        parcel_name = data['parcel_name']
        parcel_weight = data['parcel_weight']
        pick_location = data['pick_location']
        destination = data['destination']
        consignee_name = data['consignee_name']
        consignee_no = data['consignee_no']
        order_status = data['order_status']
        user_id = data['user_id']

        result = self.pac.hold(parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, user_id)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created',
                'Data': result
            }), 201)

    def get(self):
                
        pass

class ParcelList(Resource, Parcel):

    def __init__(self):

        self.pac = Parcel()


    def get(self, parcel_id):
        pass

    
    def put(self, parcel_id):
       pass
