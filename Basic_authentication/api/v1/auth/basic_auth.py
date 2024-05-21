#!/usr/bin/env python3
"""Managing API basic authentication"""
from flask import request
from typing import List, TypeVar
from .auth import Auth


class BasicAuth(Auth):
    """basic authentication"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Gets the Base64 part of the auth and returns it"""
        if authorization_header is None or \
            not isinstance(authorization_header, str) or \
                not authorization_header.startswith('Basic '):
            return None
        """otherwise return value after basic"""
        return authorization_header.split(' ')[1]
