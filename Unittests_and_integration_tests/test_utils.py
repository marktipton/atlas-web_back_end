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

    # user patch decorator to avoid making actual http requests
    @patch('utils.requests.get')
    def test_get_json(self, mock_get_method):
        """returns expected result for utils.get_json"""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        # use tuple unpacking to get test case parameters
        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get_method.return_value = mock_response

            test = get_json(test_url)

            mock_get_method.assert_called_once_with(test_url)
            # check output of json get method against test_payload
            self.assertEqual(test, test_payload)
            # reset mock so it can be used for next test case
            mock_get_method.reset_mock()


class TestMemoize(unittest.TestCase):
    """tests the memoize method of utils"""
    def test_memoize(self):
        """tests memoize function/decorator from utils"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42) as mock_method:
            # call twice
            testInstance = TestClass()
            call1 = testInstance.a_property
            call2 = testInstance.a_property

            self.assertEqual(call1, 42)
            self.assertEqual(call2, 42)
            # assert that a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
