#!/usr/bin/env python3
"""Managing API authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns true if path does not need authentication else false"""
        if (path is None or excluded_paths is None):
            return True
        if excluded_paths == []:
            return True
        # strip trailing slashes to make slash "tolerant"
        ST_path = path.rstrip('/')
        ST_excluded_paths = [p.rstrip('/') for p in excluded_paths]
        if ST_path in ST_excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None
