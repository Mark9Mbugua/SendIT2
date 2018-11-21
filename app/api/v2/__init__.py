from flask_restful import Api
from flask import Blueprint
from .views.parcel_views import ParcelView, ParcelList
from .views.user_views import UserView, SpecificUser

v2 = Blueprint('api2', __name__, url_prefix='/api/v2')

api = Api(v2)
api.add_resource(UserView, '/auth/signup')
api.add_resource(SpecificUser, '/auth/login')