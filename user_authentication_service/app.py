#!/usr/bin/env python3
"""
Flask App
"""
from auth import Auth
from os import getenv
from flask import Flask, jsonify, abort, request, make_response, redirect
from flask_cors import (CORS, cross_origin)
from user import User
import os


AUTH = Auth()
app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def jsonPayload():
    """returns JSON payload"""
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route("/users", methods=['POST'])
def users():
    """ POST /users
        register user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        # assign user instance to variable user
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registed"}), 400


@app.route("/sessions", methods=['POST'])
def login():
    """ POST /sessions
    create session for user if valid info is submitted
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({
            "email": email, "message": "logged in"
        }))
        response.set_cookie("session_id", session_id)
        return response
    abort(401)


@app.route("/sessions", methods=['DELETE'])
def logout():
    """ DELETE /sessions
        finds user with requested session id and destroys
        the session for that user if they exist
    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')

    abort(403)


@app.route("/profile", methods=['GET'])
def profile():
    """GET /profile

    """
    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route("/reset_password", methods=['POST'])
def get_reset_password_token():
    """ POST method to reset password
    """
    email = request.form.get('email')

    reset_token = AUTH.get_reset_password_token(email)
    if not reset_token:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
