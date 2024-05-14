#!/usr/bin/env python3
"""returns obfuscated log message"""
from typing import List
import re

def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:

