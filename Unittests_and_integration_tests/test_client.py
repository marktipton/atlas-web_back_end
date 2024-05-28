#!/usr/bin/env python3
"""Unittests for client
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """Tests to test_org method from client"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """test test_org method from client"""
        mock_response = {"login": org}
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org)

        # check org method:
        orgMethodresult = client.org

        # check if called once
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )
        # check that actual method result and mock response are the same
        self.assertEqual(orgMethodresult, mock_response)


if __name__ == '__main__':
    unittest.main()
