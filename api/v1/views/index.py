#!/usr/bin/python3
""" import app_views and create routes """
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def jsonstatus():
    """ return ok status """
    return jsonify(status='OK')
