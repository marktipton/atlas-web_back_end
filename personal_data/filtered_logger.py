#!/usr/bin/env python3
"""returns obfuscated log message"""
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns obfuscated information for some fields"""
    # re.sub(pattern, repl, string, count=0, flags=0)
    for field in fields:
        pattern = f'{field}=[^{separator}]*'
        obfuscated = re.sub(pattern, f'{field}={redaction}', message)
    return obfuscated
