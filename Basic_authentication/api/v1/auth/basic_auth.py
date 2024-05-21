#!/usr/bin/env python3
"""Managing API basic authentication"""
import base64
from flask import request
from typing import List, TypeVar, Tuple
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
        """otherwise return value after basic """
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns decoded value of Base64 string"""
        if base64_authorization_header is None or \
            not isinstance(base64_authorization_header, str) or \
                not base64_authorization_header:
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            decodedutf8 = decoded.decode('utf-8')
            return decodedutf8
        except Exception as e:
            pass

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """returns user email and pw from decoded b-64 value"""
        if decoded_base64_authorization_header is None or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ":" not in decoded_base64_authorization_header:
            return (None, None)
        emailpw = decoded_base64_authorization_header.split(":")
        email = emailpw[0]
        pw = emailpw[1]
        return (email, pw)
