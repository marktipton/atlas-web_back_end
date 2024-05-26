#!/usr/bin/env python3
"""
User Authentication
"""
import bcrypt
import uuid
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


def _generate_uuid() -> str:
    """returns string representation of a new uuid"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """locates user by email and then checks if password matches
            returns:
            True if match
            False in any other case
        """
        userPwBytes = password.encode('utf-8')
        user = self._db.find_user_by(email=email)
        # check if email exists
        if user:
            # check entered pw against stored pw
            if bcrypt.checkpw(userPwBytes, user.hashed_password):
                return True

        return False

    def create_session(self, email: str) -> str:
        """generates uuid for user based
        on email and stores it as the session id
        """
        user = self._db.find_user_by(email=email)
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """returns corresponding user based on session id"""

        if session_id is None:
            return None
        user = self._db.find_user_by(session_id=session_id)
        if user is None:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """destroys session by setting session id to None"""
        self._db.update_user(user_id, session_id=None)
        return None
