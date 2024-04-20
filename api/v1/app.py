#!/usr/bin/python3

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


def teardown_storage(exception):
    """Teardown method to close the storage."""
    storage.close()


app.teardown_appcontext(teardown_storage)

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
