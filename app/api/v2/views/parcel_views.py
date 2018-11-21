from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from ..models.parcel_models import Parcel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class ParcelView(Resource):
   

    def __init__(self):
        self.parcel = Parcel()
    
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        data = request.get_json()
        parcel_name = data['parcel_name']
        parcel_weight = data['parcel_weight'] 
        pick_location = data['pick_location']
        destination = data['destination']
        consignee_name = data['consignee_name']
        consignee_no = data['consignee_no']
        order_status = data['order_status']
        cost = data['cost']
        user_id = current_user["user_id"]
        
        result = self.parcel.create(parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created',
                'Data': result
            }), 201)

class UpdateParcel(Resource):

    def __init__(self):
        self.parcel =  Parcel()
    
    @jwt_required
    def put(self, parcel_id):
        current_user = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument('destination', help = "Kindly Fill in ", required=True)
        parser.add_argument('user_id', help = "Kindly Fill in", required=True)
        data = parser.parse_args()
        destination = data['destination']
        user_id = current_user["user_id"]
        update_parcel = self.parcel.updateParcel(destination, parcel_id, user_id)   
        if update_parcel:  
                
            return make_response(jsonify(
                    {
                        'Response': "Destination changed successfully",
                        'Data': update_parcel
                    }), 200)
       
        return make_response(jsonify(
            {
                'Response': 'Parcel not found'
        
            }), 404)