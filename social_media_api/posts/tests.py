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

    
class FeedTests(APITestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(username='u1', password='pass')
        self.user2 = get_user_model().objects.create_user(username='u2', password='pass')
        self.client.force_authenticate(user=self.user1)
        self.user1.following.add(self.user2)
        self.post1 = Post.objects.create(author=self.user1, title='P1', content='C1')
        self.post2 = Post.objects.create(author=self.user2, title='P2', content='C2')

    def test_feed(self):
        response = self.client.get('/api/feed/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)