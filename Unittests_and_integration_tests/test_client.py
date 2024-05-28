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

    def test_public_repos_url(self):
        """unit-test fpr GithubOrgClient _public_repos_url property"""

        # known payload containig expected value for _public_repos_url
        test_payload = {"test_url": "http://example.com/test"}

        # patch the org method of GithubOrgClient so that the mocked method is
        # called instead of the actual method
        with patch.object(GithubOrgClient, 'org') as mock_org:
            mock_org.return_value = test_payload

            client = GithubOrgClient("example_org")

            result = client._public_repos_url

            self.assertEqual(result, test_payload["test_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_repo_url, mock_get_json):
        """test for public_repos method in client"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]

        mock_repo_url.return_value = "http://example.com/test"

        mock_get_json.return_value = mock_payload

        client = GithubOrgClient("example_org")

        repo = client.public_repos()
        # check that result is the list of repos from the mock payload
        self.assertEqual(repo, ["repo1", "repo2"])

        # check that _public_repos_url was only called once
        mock_repo_url.assert_called_once()

        # check that get_json was called once with mocked url
        mock_get_json.assert_called_once_with("http://example.com/test")


if __name__ == '__main__':
    unittest.main()