from flask import Flask, Blueprint
from .api.v1 import v1
from instance.config import app_config


def make_app(config_name):
    app = Flask(__name__)

    
    app.register_blueprint(v1)

    return app