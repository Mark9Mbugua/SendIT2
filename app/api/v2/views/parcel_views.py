from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from ..models.parcel_models import Parcel
from ..models.user_models import User
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


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

        result = self.parcel.create(parcel_name, parcel_weight, pick_location,
                                    destination, consignee_name, consignee_no, order_status, cost, user_id)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created successfully',
                'Data': result
            }), 201)
    
    def get(self):
        all_parcels = self.parcel.getAllParcels()
        if all_parcels is not None:
            
            return make_response(jsonify(
                {
                    'Response': "Here are all the parcels",
                    'status': "OK",
                    'Data': all_parcels
                }), 200)
        
        return make_response(jsonify({
            'Response' : "Parcels not found",

        }), 404)
        



class UpdateParcel(Resource):

    def __init__(self):
        self.parcel = Parcel()
        self.user = User()

    @jwt_required
    def put(self, parcel_id):
        current_user = get_jwt_identity()
        user_id = current_user['user_id']

        if current_user["role"] == "User":
            parser = reqparse.RequestParser()
            parser.add_argument('destination', help="Kindly provide new destination ", required=True)
            data = parser.parse_args()
            destination = data['destination']
            parcel_id = int(parcel_id)
            update_parcel = self.parcel.updateParcel(destination, parcel_id, user_id)
            
            if update_parcel is not None:
                return make_response(jsonify(
                        {
                            'Response': "Destination changed successfully",
                            'Data': update_parcel
                        }), 200)

            return make_response(jsonify(
                {
                    'Response': 'Parcel not found'

                }), 404)
        
        return make_response(jsonify(
                {
                    'Response': 'User not authorized to make this request'

                }), 400)


class UserParcels(Resource):
    
    def __init__(self):
        self.parcel = Parcel()
        self.user = User()
    
    @jwt_required
    def get(self, user_id):
        current_user = get_jwt_identity()
        user_id = current_user['user_id']

        if current_user["role"] == "User":
            user_parcels = self.parcel.getUserParcels(user_id)
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
        
        return make_response(jsonify(
                {
                    'Response': 'User not authorized to make this request'

                }), 400)

