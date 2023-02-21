# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.user_profile import UserProfile  # noqa: E501
from openapi_server.test import BaseTestCase


class TestUserProfileController(BaseTestCase):
    """UserProfileController integration test stubs"""

    def test_create_user_profile(self):
        """Test case for create_user_profile

        Create a new user-profile
        """
        user_profile = {"name":"name","email":"email"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/UserProfile',
            method='POST',
            headers=headers,
            data=json.dumps(user_profile),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user_profile(self):
        """Test case for delete_user_profile

        Delete the current user-profile. Note this is permanent!
        """
        headers = { 
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/UserProfile',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_describe_user_profile(self):
        """Test case for describe_user_profile

        Read the current user-profile
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/UserProfile',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user_profile(self):
        """Test case for update_user_profile

        Update the current user-profile
        """
        user_profile = {"name":"name","email":"email"}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/UserProfile',
            method='PUT',
            headers=headers,
            data=json.dumps(user_profile),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
