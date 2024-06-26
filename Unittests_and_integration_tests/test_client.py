#!/usr/bin/env python3
"""Unittests for client
"""
import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock


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
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            client = GithubOrgClient("example_org")

            result = client._public_repos_url

            self.assertEqual(result, test_payload["test_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test for public_repos method in client"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]

        mock_get_json.return_value = mock_payload

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = "http://example.com/test"
            client = GithubOrgClient("example_org")

            repo = client.public_repos()
            # print(repo)
            # print(["repo1", "repo2"])
            # check that result is the list of repos from the mock payload
            self.assertEqual(repo, ["repo1", "repo2"])

            # check that _public_repos_url was only called once
            mock_repo_url.assert_called_once()

            # check that get_json was called once with mocked url
            mock_get_json.assert_called_once_with("http://example.com/test")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license, expected):
        """test has_license method of GithubOrgClient"""
        client = GithubOrgClient("example_org")

        test_result = client.has_license(repo, license)

        # compare expected result to has_license function call result
        self.assertEqual(test_result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for public repos method"""
    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    @classmethod
    def setUpClass(cls):
        """set up test class"""
        cls.get_patcher = patch(
            'requests.get',
            side_effect=cls.mock_get
        )
        # start patcher
        cls.mock_get = cls.get_patcher.start()
        # define side effects to return fixtures corresponding to URLS

    @classmethod
    def tearDownClass(cls):
        """tear down test class"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
