#!/usr/bin/python3
"""Starts API"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from api.v1.views import state_views


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')
app.register_blueprint(state_views, url_prefix='/api/v1/states')


@app.teardown_appcontext
def close_storage(exception):
    """Closes Storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 errors"""
    response = {"error": "Not found"}
    return (jsonify(response), 404)


if __name__ == "__main__":
    from os import getenv
    # Fetch host and port from environment variables or use defaults
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True, debug=True)
