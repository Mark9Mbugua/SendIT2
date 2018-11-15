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

        if result is not None:

            return make_response(jsonify(
                {
                    'Response': 'Parcel Created',
                    'Data': result
                }), 201)
                

    def get(self):        
        parcels = self.pac.getparcels()

        return make_response(jsonify(
                {
                    'Response': "Parcels Ready",
                    'Data': parcels 
                }), 200)

class ParcelList(Resource, Parcel):

    def __init__(self):

        self.pac = Parcel()


    def get(self, parcel_id):
        p_id = int(parcel_id)
        parcel = self.pac.getparcel(p_id) 

        if parcel is not None:
            return make_response(jsonify(
                {
                    'Response': "Parcel is Ready",
                    'Data': parcel
                }), 200)
        return make_response(jsonify(
            {
                "Status": "Not Found"
            }
        ))

    
    def put(self, parcel_id):
        p_id = int(parcel_id)
        parcel = self.pac.cancelparcel(p_id) 
        return make_response(jsonify(
                {
                    'Response': "Order Status Updated",
                    'Data': parcel
                }), 200)         

class ParcelsForUser(Resource, Parcel):

    def __init__(self):
        self.pac =  Parcel()
    
    def get(self, user_id):
        u_id = int(user_id)
        usrparcels = self.pac.getuserparcels(u_id)
        return make_response(jsonify(
                {
                    'Response': "User's parcels ready",
                    'Data': usrparcels
                }), 200)

