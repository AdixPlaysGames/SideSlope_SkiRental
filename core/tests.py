from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345') #ciekawe rzeczy z haslem

    def test_index_view(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_about_view(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view(self):
        response = self.client.get(reverse('core:contact'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view(self):
        response = self.client.get(reverse('core:signup'))
        self.assertEqual(response.status_code, 200)

    def test_pricing_view_without_login(self):
        response = self.client.get(reverse('core:pricing'))
        self.assertEqual(response.status_code, 302)

    def test_rented_items_view_without_login(self):
        response = self.client.get(reverse('core:rented_items'))
        self.assertEqual(response.status_code, 302)