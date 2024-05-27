#!/usr/bin/env python3
"""Unittests for utils
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized



class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access nested map function"""

    @parameterized.expand([
        nested_map={"a": 1}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a",)
        nested_map={"a": {"b": 2}}, path=("a", "b")
    ])
    def test_access_nested_map():

