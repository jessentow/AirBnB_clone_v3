#!/usr/bin/python3
"""Index of api"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review

# app_views.url_map.strict_slashes = False


@app_views.route('/status')
def check_status():
    """Return status"""
    return (jsonify({"status": "OK"}))


@app_views.route('/stats')
def count_object():
    """Retrieves the number of each object by type"""
    data = {"amenities": 0, "cities": 0, "places": 0, "reviews": 0,
            "states": 0, "users": 0}

    for key in data.keys():
        if key == "amenities":
            data[key] = storage.count(Amenity)
        elif key == "states":
            data[key] = storage.count(State)
        elif key == "cities":
            data[key] = storage.count(City)
        elif key == "places":
            data[key] = storage.count(Place)
        elif key == "users":
            data[key] = storage.count(User)
        elif key == "reviews":
            data[key] = storage.count(Review)
    return (jsonify(data))
