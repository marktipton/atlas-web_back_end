#!/usr/bin/env python3
"""
Flask App
"""
from auth import Auth
from os import getenv
from flask import Flask, jsonify, abort, request, make_response
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
