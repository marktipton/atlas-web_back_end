#!/usr/bin/env python3
"""Managing API session authentication"""
import base64
import logging
from flask import request
from typing import List, TypeVar, Tuple
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session Authentication class"""

