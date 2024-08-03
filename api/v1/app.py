#!/usr/bin/python3
"""Api app v1 module """


from flask import Flask
from models import storage
from api.v1.views import app_views
from os import environ

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """Tears down app """
    storage.close()


if __name__ == "__main__":
    Host = environ.get('HBNB_API_HOST')
    if not Host:
        host = '0.0.0.0'
    Port = environ.get('HBNB_API_PORT')
    if not Port:
        port = '5000'

    app.run(host=Host, port=Port, threaded=True)
