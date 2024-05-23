#!/usr/bin/env python3
""" Module for session auth views
"""
from flask import jsonify, abort, request, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route(
    '/api/v1/auth_session/login',
    methods=['POST'],
    strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - JSON response with the User data and set session cookie
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.id)

        response = make_response(user.to_json())
        session_name = getenv('SESSION_NAME', '_my_session_id')
        response.set_cookie(session_name, session_id)

        return response
