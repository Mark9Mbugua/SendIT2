from flask_restful import Resource
from flask import jsonify, make_response, request

from ..models.parcel_models import Parcel


class ParcelView(Resource):
   

    def __init__(self):
        self.parcel = Parcel()

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
        
        result = self.parcel.create(parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, user_id)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created',
                'Data': result
            }), 201)
        

    def get(self):        
        parcels = self.parcel.getParcels()

        if parcels is not None:

            return make_response(jsonify(
                    {
                        'Response': "Parcels Ready",
                        'Data': parcels 
                    }), 200)
        
        return make_response(jsonify(
            {
                'Response': 'Parcels not found'
        
            }), 400)

class ParcelList(Resource):

    def __init__(self):

        self.parcel = Parcel()


    def get(self, parcel_id):
        p_id = int(parcel_id)
        parcel = self.parcel.getParcel(p_id) 

        if parcel is not None:
            return make_response(jsonify(
                {
                    'Response': "Parcel is Ready",
                    'Data': parcel
                }), 200)
        
        return make_response(jsonify(
            {
                'Response': 'Parcel not found'
        
            }), 400)


class CancelParcel(Resource): 

    def __init__(self):
        self.parcel = Parcel()

    def put(self, parcel_id):
        p_id = int(parcel_id)
        parcel = self.parcel.cancelParcel(p_id) 

        if parcel is not None:

            return make_response(jsonify(
                    {
                        'Response': "Order Status Updated",
                        'Data': parcel
                    }), 200)
        
        return make_response(jsonify(
            {
                'Response': 'Parcel to be cancelled not found'
        
            }), 404)         

class UserParcels(Resource):

    def __init__(self):
        self.parcel =  Parcel()
    
    def get(self, user_id):
        u_id = int(user_id)
        user_parcels = self.parcel.getUserParcels(u_id)

        if user_parcels is not None:  
                
            return make_response(jsonify(
                    {
                        'Response': "User's parcels ready",
                        'Data': user_parcels
                    }), 200)
       
        return make_response(jsonify(
            {
                'Response': 'User not found'
        
            }), 404)
