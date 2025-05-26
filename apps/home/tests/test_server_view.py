from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from core import settings


class MyTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('servers')
        self.client.force_login(self.user)

    def test_view_url_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/servers.html')

    def test_segment_in_context(self):
        response = self.client.get(self.url)

        self.assertEqual(response.context['segment'], 'servers')
        self.assertEqual(response.context['url'], settings.DISPLAY_SERVER_IP)

        self.assertTrue(response.context['status'])

        self.assertIsInstance(response.context['running'], list)
        self.assertIsInstance(response.context['exited'], list)





