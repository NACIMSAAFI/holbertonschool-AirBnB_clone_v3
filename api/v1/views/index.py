#!/usr/bin/python3
"""
This module contains the status route
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User



@app_views.route("/status", methods=["GET"], strict_slashes=False)
def get_status():
    """
    Return the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"], strict_slashes=False)
def get_stats():
    """
    Return the number of objects by type
    """
    total_objects = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User),
    }

    return jsonify(total_objects)
