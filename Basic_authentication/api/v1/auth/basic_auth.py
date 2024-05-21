#!/usr/bin/env python3
"""Managing API basic authentication"""
from flask import request
from typing import List, TypeVar
from auth import Auth


class BasicAuth(Auth):
    """basic authentication"""
