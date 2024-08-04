#!/usr/bin/python3
"""Renders blue print"""
from flask import Blueprint

app_view = Blueprint("app_view", __name__, url_prefix='/api/vi')

from api.v1.views.index import *
