#!/usr/bin/python3
"""Index of api"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def app_status():
    """Return status"""
    return (jsonify({"status": "OK"}))
