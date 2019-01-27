import re
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request, abort
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
        if current_user["role"] == "User":
            parser = reqparse.RequestParser()
            parser.add_argument('parcel_name', help = "cannot be blank", required=True)
            parser.add_argument('parcel_weight', help = "cannot be blank", required=True)
            parser.add_argument('pick_location', help = "cannot be blank", required=True)
            parser.add_argument('destination', help = "cannot be blank", required=True)
            parser.add_argument('present_location', help = "cannot be blank", required=True)
            parser.add_argument('consignee_name', help = "cannot be blank", required=True)
            parser.add_argument('consignee_no', help = "cannot be blank", required=True)
            parser.add_argument('order_status', help = "cannot be blank", required=True)
            parser.add_argument('cost', help = "cannot be blank", required=True)

            data = parser.parse_args()
            
            parcel_name = data['parcel_name']
            parcel_weight = data['parcel_weight']
            pick_location = data['pick_location']
            destination = data['destination']
            present_location = data['present_location']
            consignee_name = data['consignee_name']
            consignee_no = data['consignee_no']
            order_status = data['order_status']
            cost = data['cost']
            user_id = current_user["user_id"]
            
            if parcel_weight.isdigit() is False:
                return {'Message': "Parcel weight must have numbers only"}, 400
            
            if cost.isdigit() is False:
                return {'Message': "Cost must have numbers only"}, 400
            
            if consignee_no.isdigit() is False:
                return {'Message': "Consignee's phone number must have numbers only"}, 400

            if not re.search('[A-Za-z]', parcel_name):
                return {'Message': "Parcel's name should have letters"}, 400
            
            if not re.search('[A-Za-z]', pick_location):
                return {'Message': "Pick-up location should have letters"}, 400
            
            if not re.search('[A-Za-z]', destination):
                return {'Message': "Destination should have letters"}, 400
            
            if not re.search('[A-Za-z]', present_location):
                return {'Message': "Present location should have letters"}, 400
            
            if not re.search('[A-Za-z]', consignee_name):
                return {'Message': "Consignee's name should have letters"}, 400
            
            result = self.parcel.create(parcel_name=parcel_name, parcel_weight=int(parcel_weight), pick_location=pick_location,
                                        destination=destination, present_location=present_location, consignee_name=consignee_name, 
                                        consignee_no=int(consignee_no), order_status=order_status, cost=int(cost), user_id=int(user_id))
            
            return make_response(jsonify(
                {
                    'Response': 'Parcel Created successfully',
                    'Data': result,

                    'Status': "OK"
                }), 201)
        
        return {'Message': "Sorry, request cannot be completed for this user"}, 401
        
    
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        if current_user ['role'] == "Admin":
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
            
        return make_response(jsonify({
                'Response' : "Sorry, request cannot be completed for this user",

            }), 401)
        
        

class ParcelList(Resource):
    def __init__(self):
        self.parcel = Parcel()
    
    def get(self, parcel_id):
        parcel = self.parcel.getOneParcel(parcel_id)
        if parcel:
            return make_response(jsonify({
                'Response': "Parcel Ready",
                'Data': parcel,
                'status': 'OK'
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

class UpdateLocation(Resource):

    def __init__(self):
        self.parcel = Parcel()
        self.user = User()

    @jwt_required
    def put(self, parcel_id):
        current_user = get_jwt_identity()
        user_id = current_user['user_id']

        if current_user["role"] == "Admin":
            parser = reqparse.RequestParser()
            parser.add_argument('present_location', help="Kindly provide parcel's present location ", required=True)
            data = parser.parse_args()
            present_location = data['present_location']
            parcel_id = int(parcel_id)
            update_location = self.parcel.updateLocation(present_location, parcel_id, user_id)
            
            if parcel_id:
                return make_response(jsonify(
                        {
                            'Response': "Location updated successfully",
                            'Data': update_location
                        }), 200)

            return make_response(jsonify(
                {
                    'Response': 'Parcel not found'

                }), 404)
        
        return make_response(jsonify(
                {
                    'Response': 'User not authorized to make this request'

                }), 400)
    
class UpdateOrderStatus(Resource):

    def __init__(self):
        self.parcel = Parcel()
        self.user = User()

    @jwt_required
    def put(self, parcel_id):
        current_user = get_jwt_identity()
        user_id = current_user['user_id']

        if current_user["role"] == "Admin":
            parser = reqparse.RequestParser()
            parser.add_argument('order_status', help="Kindly provide parcel's latest order status ", required=True)
            data = parser.parse_args()
            order_status = data['order_status']
            parcel_id = int(parcel_id)
            update_order_status = self.parcel.updateOrderStatus(order_status, parcel_id, user_id)
            
            if parcel_id:
                return make_response(jsonify(
                        {
                            'Response': "Order Status updated successfully",
                            'Data': update_order_status
                        }), 200)

            return make_response(jsonify(
                {
                    'Response': 'Parcel not found'

                }), 404)
        
        return make_response(jsonify(
                {
                    'Response': 'User not authorized to make this request'

                }), 400)

