#!/usr/bin/env python3
"""Managing API session authentication"""
import base64
import logging
import uuid
from flask import request
from typing import List, TypeVar, Tuple
from .auth import Auth
from models.user import User


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
