#!/usr/bin/python3
"""Creates a new view for State objects that handles
all default RESTFul API actions:
"""
from models.state import State
from models import storage
from api.v1.views import state_views
from flask import jsonify

all_states = storage.all(State)


@state_views.route('/')
def get_states():
    """Retrieves the list of all State objects"""
    state_list = []
    for key, value in all_states.items():
        state_list.append(value.to_dict())
    return (jsonify(state_list))


@state_views.route('/')
def get_object():
