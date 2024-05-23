#!/usr/bin/env python3
"""Managing API session authentication"""
import base64
import logging
import requests
import uuid
from flask import jsonify, abort, request
from typing import List, TypeVar, Tuple
from .auth import Auth
from models.user import User
from os import getenv


class SessionAuth(Auth):
    """Session Authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates session ID for a user ID"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns a User based on a cookie value"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None):
        """deletes the user session"""
        id = request.cookies.id
        if request is None or id is None or \
                self.user_id_for_session_id(id) is None:
            return False
        del self.user_id_by_session_id(id)
        return True
