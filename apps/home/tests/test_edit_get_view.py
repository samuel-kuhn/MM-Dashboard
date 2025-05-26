from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from ..api_functions import create
from ..utilities import get_user_profile_details

class MyTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('edit')
        self.client.force_login(self.user)

    def test_view_url_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/edit.html')

    def test_segment_in_context_server_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.context['segment'], 'edit')

        self.assertTrue(response.context['overview'])

        self.assertIsInstance(response.context['servers'], list)

    def test_segment_in_context_form_view(self): # giving exception for nonexistent server
        data = {
            "csrfmiddlewaretoken": 'some token',
            "server_name": 'testserver',
            "PORT": "25565",
            "VERSION": "1.16.5",
            "MODE": "survival",
            "MEMORY": "2G",
            "MOTD": "just a testserver"
        }

        create(self.user.username, data)

        response = self.client.get(self.url + '?server=testserver')

        self.assertEqual(response.context['segment'], 'edit')

        # user profile
        user_data = get_user_profile_details(self.user.username)
        self.assertEqual(response.context['max_ram'], user_data["max_ram"])
        self.assertEqual(response.context['ram_list'], user_data["ram_list"])
        self.assertEqual(response.context['port_list'], user_data["port_list"])

        # server profile
        self.assertEqual(response.context['NAME'], data["server_name"])
        self.assertEqual(response.context['MEMORY'], data["MEMORY"].split('G')[0])
        self.assertEqual(response.context["MOTD"], data["MOTD"])
        self.assertEqual(response.context['MODE'], data["MODE"])
        self.assertEqual(response.context['VERSION'], data["VERSION"])
        self.assertEqual(response.context['PORT'], data["PORT"])




