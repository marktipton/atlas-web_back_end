#!/usr/bin/env python3
"""
User Authentication
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes pw and returns salted hash version"""
    # convert pw to an array of bytes
    byteConversion = password.encode('utf-8')

    # generate random data for hashing function
    salt = bcrypt.gensalt()

    hashedPassword = bcrypt.hashpw(byteConversion, salt)

    return(hashedPassword)
