#!/usr/bin/env python3
"""Unittests for client
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Tests to test_org method from client"""
    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch('get_json')
    def test_org(self, org):
        """test test_org method from client"""
        self.assertEqual(GithubOrgClient.org(org))

