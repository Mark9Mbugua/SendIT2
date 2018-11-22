from flask_restful import Api
from flask import Blueprint
from .views.parcel_views import ParcelView, UpdateParcel
from .views.user_views import Register, Login

v2 = Blueprint('api2', __name__, url_prefix='/api/v2')

api = Api(v2)
api.add_resource(Register, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(ParcelView, '/parcels')
api.add_resource(UpdateParcel, '/parcels/<int:parcel_id>/destination')
