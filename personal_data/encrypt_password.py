#!/usr/bin/env python3
"""
Password ENcryption using hashing.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns hashed and salted password"""
    # convert pw to an array of bytes
    byteConversion = password.encode('utf-8')

    # generate random data for hashing function
    salt = bcrypt.gensalt()

    hashedPassword = bcrypt.hashpw(byteConversion, salt)

    return(hashedPassword)
