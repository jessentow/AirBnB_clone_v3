#!/usr/bin/python3
"""Renders blue print"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__)
state_views = Blueprint("state_views", __name__)

from api.v1.views.index import *
from api.v1.views.states import *
