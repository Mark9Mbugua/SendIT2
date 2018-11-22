from flask_restful import Resource
from flask import jsonify, make_response, request
from ..models.parcel_models import Parcel
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


class ParcelView(Resource):
   

    def __init__(self):
        self.parcel = Parcel()
    @jwt_required
    def post(self):
        data = request.get_json()
        parcel_name = data['parcel_name']
        parcel_weight = data['parcel_weight'] 
        pick_location = data['pick_location']
        destination = data['destination']
        consignee_name = data['consignee_name']
        consignee_no = data['consignee_no']
        order_status = data['order_status']
        cost = data['cost']
        user_id = data['user_id']
        
        result = self.parcel.create(parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost, user_id)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created',
                'Data': result
            }), 201)

