#!/usr/bin/python3
"""
Creates a new view for State objects that handles
all default RESTFul API actions:
"""

from models.state import State
from models import storage
from api.v1.views import state_views
from flask import jsonify, request, abort


@state_views.route('/')
def list_states():
    """Retrieves the list of all State objects"""
    all_states = storage.all(State)
    state_list = []
    for key, value in all_states.items():
        state_list.append(value.to_dict())
    return (jsonify(state_list))


@state_views.route('/<state_id>')
def get_state(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return (jsonify(state.to_dict()))


@state_views.route('/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return (jsonify({}), 200)


@state_views.route('/', methods=['POST'])
def create_state():
    """Creates a state object using POST"""
    if not request.json:
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing name")
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    return (jsonify(new_state.to_dict()), 201)


@state_views.route('/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a state object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.json:
        abort(400, "Not a JSON")
    data = request.get_json()
    if "name" not in data:
        abort(400, "Missing name")
    state.name = data['name']
    storage.save()
    return (jsonify(state.to_dict()), 200)
