import os

from app import make_app

config_name = os.getenv('APP_SETTINGS')

app = make_app(config_name)

if __name__ == '__main__':
    app.run(debug=True )