#!/usr/bin/python3
"""Index of api"""
from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


@app_views.route('/status')
def check_status():
    """Return status"""
    return (jsonify({"status": "OK"}))


@app_views.route('/stats', methods=['GET'])
def count_object():
    """Retrieves the number of each object by type"""
    count_data = {}
    data = {"amenities": "Amenity", "cities": "City", "places": "Place",
            "reviews": "Review", "states": "State", "users": "User"}
    for key, value in data.items():
        count_data[key] = storage.count(value)
    return (make_response(jsonify(count_data)))
