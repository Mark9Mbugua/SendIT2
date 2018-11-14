from flask_restful import Resource
from flask import jsonify, make_response, request, sessions

from ..models.parcel_models import Parcel


class ParcelView(Resource, Parcel):
   

    def __init__(self):
        self.pac = Parcel()

    def post(self):
        pass

    def get(self):
                
        pass

class ParcelList(Resource, Parcel):

    def __init__(self):

        self.pac = Parcel()


    def get(self, parcel_id):
        pass

    
    def put(self, parcel_id):
       pass
