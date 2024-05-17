#!/usr/bin/env python3
"""returns obfuscated log message"""
from mysql.connector.connection import MySQLConnection
from typing import List, Optional
import logging
import os
import re
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns obfuscated information for some fields"""
    # re.sub(pattern, repl, string, count=0, flags=0)
#     for field in fields:
#         pattern = f'{field}=[^{separator}]*'
#         obfuscated = re.sub(pattern, f'{field}={redaction}', message)
#     return obfuscated
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(
        pattern, lambda x: x.group().split('=')[0] + '=' + redaction,
        message
        )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters specified fields and obfuscates values"""
        message = record.msg
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  message, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)

#  create streamHandler and set its format to RedactingFormatter
    handler = logging.StreamHandler()
    formatting = RedactingFormatter()
    handler.setFormatter(formatting)

#     add handler to logger
    logger.addHandler(handler)
#     stop logger from giving info to other loggers
    logger.propagate = False
    return logger


def get_db() -> MySQLConnection:
    """returns a connector to the sequel database"""
    # print(os.environ['HOME'])
    # return os.environ['HOME']
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    databasename = os.getenv('PERSONAL_DATA_DB_NAME')
    connector = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=databasename
    )
    return connector
