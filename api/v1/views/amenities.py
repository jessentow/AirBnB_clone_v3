#!/usr/bin/python3
"""
Creates a new view for Amenity objects that handles
all default RESTFul API actions:
"""

from models.amenity import Amenity
from models import storage
from api.v1.views import amenity_views
from flask import jsonify, request, abort


@amenity_views.route('/')
def list_amenities():
    """Retrieves the list of all amenities objects"""
    all_amenities = storage.all(Amenity)
    amenities_list = []
    for key, value in all_amenities.items():
        amenities_list.append(value.to_dict())
    return (jsonify(amenities_list))


@amenity_views.route('/<amenity_id>')
def get_amenity(amenity_id):
    """Retrieves a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return (jsonify(amenity.to_dict()))


@amenity_views.route('/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Deletes an Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return (jsonify({}), 200)


@amenity_views.route('/', methods=['POST'])
def create_amenity():
    """Creates a amenity object using POST"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing name")
    new_amenity = Amenity(**data)
    storage.new(new_amenity)
    storage.save()
    return (jsonify(new_amenity.to_dict()), 201)


@amenity_views.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing name")
    amenity.name = data['name']
    storage.save()
    return (jsonify(amenity.to_dict()), 200)
