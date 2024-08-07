#!/usr/bin/python3
"""
Creates a new view for City objects that handles
all default RESTFul API actions:
"""
from models.state import City
from models import storage
from api.v1.views import city_views
from flask import jsonify, request, abort


