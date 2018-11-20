from flask_restful import Api
from flask import Blueprint

v2 = Blueprint('api2', __name__, url_prefix='/api/v2')


api = Api(v2)
