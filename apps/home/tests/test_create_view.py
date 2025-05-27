from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class CreateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('create')
        self.client.force_login(self.user)

    def test_view_url_exists(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/create.html')

    def test_segment_in_context(self):
        response = self.client.get(self.url)

        self.assertEqual(response.context['segment'], 'create')
        self.assertEqual(response.context['port_list'], ['25565', '25566', '25567', '25568'])
        self.assertEqual(response.context['max_ram'], 5)
        self.assertEqual(response.context['ram_list'], ['1', '2', '3', '4', '5'])





