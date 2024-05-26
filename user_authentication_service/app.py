#!/usr/bin/env python3
"""
Flask App
"""
from auth import Auth
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
