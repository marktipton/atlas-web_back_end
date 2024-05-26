#!/usr/bin/env python3
"""
User Authentication
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """takes pw and returns salted hash version"""
    # convert pw to an array of bytes
    byteConversion = password.encode('utf-8')

    # generate random data for hashing function
    salt = bcrypt.gensalt()

    hashedPassword = bcrypt.hashpw(byteConversion, salt)

    return(hashedPassword)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user by hashing pw if the user doesnt already exist"""
        if self._db.find_user_by(email=email):
            raise ValueError(f"User {email} already exists")

        hashed_pw = _hash_password(password)
        registered_user = self._db.add_user(email, hashed_pw)
        return registered_user
