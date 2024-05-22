#!/usr/bin/env python3
"""Managing API basic authentication"""
import base64
from flask import request
from typing import List, TypeVar, Tuple
from .auth import Auth
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns user instance based on email and pw"""
        if user_email is None or not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_pwd, str):

            return None

        try:
            users = User.search({'email': user_email})
        except Exception as e:
            return None

        if not users:
            return None
        # check if user passwords match
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        # return none if not valid PW
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads auth current user class and
            retrieves User instance for request
        """
        auth_header = super().authorization_header(request)
        if auth_header is None:
            return None
        extract = self.extract_base64_authorization_header(auth_header)
        if extract is None:
            return None
        decode = self.decode_base64_authorization_header(extract)
        if decode is None:
            return None
        extractUser = self.extract_user_credentials(decode)
        if extractUser is None:
            return None
        userObject = self.user_object_from_credentials(extractUser)

        return userObject
