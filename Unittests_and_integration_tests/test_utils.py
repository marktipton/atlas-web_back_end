#!/usr/bin/env python3
"""Unittests for utils
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock



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
    # check if key error is raised when nested map does not exist
        ({}, ("a",)),
    # check if key error when key's value is not a dictionary
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that KeyError is raised"""
        # with sets up context for code block that follows
        # if KeyError is raised the the context manager catches it
        # i.e. the test passes if a keyerror is raised
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for get_json method in utils"""
    @patch('utils.requests.get')
    def test_get_json():

        """returns expected result for utils.get_json"""

