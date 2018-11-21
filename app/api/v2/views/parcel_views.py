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
        cost = data['cost']
        
        result = self.parcel.create(parcel_name, parcel_weight, pick_location, destination, consignee_name, consignee_no, order_status, cost)

        return make_response(jsonify(
            {
                'Response': 'Parcel Created',
                'Data': result
            }), 201)

