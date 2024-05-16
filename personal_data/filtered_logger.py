#!/usr/bin/env python3
"""returns obfuscated log message"""
from typing import List
import logging
import re


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
        message = record.msg
        record.msg = filter_datum(self.fields, self.REDACTION,
                        message, self.SEPARATOR)
        return record.msg
