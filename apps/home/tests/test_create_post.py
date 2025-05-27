from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from ..api_functions import get_servers, delete
from ..pages import *

data = {
    "csrfmiddlewaretoken": "some token",
    "server_name": "testserver",
    "PORT": "25565",
    "VERSION": "1.16.5",
    "MODE": "survival",
    "MEMORY": "2G",
    "MOTD": "just a testserver"
}


def delete_all_servers(user):
    for server in get_servers(user):
        delete(user, server["NAME"])


class CreatePostTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('create')
        self.client.force_login(self.user)

    def test_view_returns_500_on_empty_post(self):
        # ACT
        response = self.client.post(self.url)

        # ASSERT
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ERROR_PAGE)

    def test_view_create_server_already_existing(self):
        # ARRANGE
        delete_all_servers(self.user.username)

        # ACT
        self.client.post(self.url, data=data)
        response = self.client.post(self.url, data=data)

        # ASSERT
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ERROR_PAGE)

    def test_view_create_server_bad_data(self):
        # ARRANGE
        delete_all_servers(self.user.username)

        bad_data = data
        bad_data["server_name"] = " "

        # ACT
        response = self.client.post(self.url, data=data)

        # ASSERT
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, ERROR_PAGE)

    def test_view_create_server_successful(self):
        # ARRANGE
        delete_all_servers(self.user.username)

        # ACT
        response = self.client.post(self.url, data=data)

        # ASSERT
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('servers'))  # redirects to home screen

        self.assertEqual(len(get_servers(self.user.username)), 1)
