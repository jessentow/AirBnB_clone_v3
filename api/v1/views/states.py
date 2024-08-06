#!/usr/bin/python3
"""Creates a new view for State objects that handles
all default RESTFul API actions:
"""
from models.state import State
from models import storage
from api.v1.views import state_views
from flask import jsonify, make_response


@state_views.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors"""
    response = {"error": "Not found"}
    return (make_response(jsonify(response), 404))


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

    return (page_not_found(404))


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
            return (make_response(jsonify({}), 200))
    return (page_not_found(404))
