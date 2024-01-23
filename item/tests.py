from django.test import TestCase, Client
from django.urls import reverse
from .models import Item, Category
from django.contrib.auth.models import User

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345') #ciekawe rzeczy z haslem
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(
            name='Test Item', 
            category=self.category, 
            price=10.0
        )

    def test_about_view(self):
        response = self.client.get(reverse('item:detail'))
        self.assertEqual(response.status_code, 200)