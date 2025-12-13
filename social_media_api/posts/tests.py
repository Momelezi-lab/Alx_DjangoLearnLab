from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test')
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(author=self.user, title='Test', content='Test')

    def test_create_post(self):
        response = self.client.post('/api/posts/', {'title': 'New', 'content': 'New'})
        self.assertEqual(response.status_code, 201)

    
