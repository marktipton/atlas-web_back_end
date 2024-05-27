#!/usr/bin/env python3
"""Unittests for utils
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized



class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access nested map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """check return of access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
