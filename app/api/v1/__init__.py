from flask_restful import Api
from flask import Blueprint

from .views.parcel_views import ParcelView, ParcelList, ParcelsForUser
from .views.user_views import UserView, SpecificUser

v1 = Blueprint('api1', __name__, url_prefix='/api/v1')

api = Api(v1)

api.add_resource(ParcelView, '/parcels')
api.add_resource(ParcelList, '/parcels/<int:parcel_id>')
api.add_resource(ParcelsForUser, '/users/<int:user_id>/parcels')
api.add_resource(UserView, '/signup')
api.add_resource(SpecificUser, '/login')