#!/usr/bin/env python3
"""
Flask App
"""
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def jsonPayload():
    """returns JSON payload"""
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
