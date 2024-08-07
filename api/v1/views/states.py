#!/usr/bin/python3
"""Creates a new view for State objects that handles
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
    all_states = storage.all(State).values()
    for state in all_states:
        current_state = state.to_dict()
        current_state_id = current_state.get('id')
        if current_state_id == state_id:
            return (jsonify(current_state))
    abort(404)


@state_views.route('/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a state object"""
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    state_obj.remove(state_obj[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
            return (jsonify({}), 200)
    abort(404)


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
