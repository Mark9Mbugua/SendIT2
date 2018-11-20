from flask import Flask, Blueprint
from .api.v2 import v2
from .db_config import create_tables, destroy_tables, init_db

def make_app(config_name):
    app = Flask(__name__)
    init_db()
    # destroy_tables()
    create_tables()
    app.register_blueprint(v2)

    return app