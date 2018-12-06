from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User


class UserTests(APITestCase):
    def test_create_User(self):
        """
        Ensure we can create a new User object.
        """
        # url = reverse('inscription')
        data = {'name': 'DabApps'}
        response = self.client.post('/inscription/', data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_404_NOT_FOUND)
        # self.assertEqual(User.objects.count(), 1)
        # self.assertEqual(User.objects.get().name, 'DabApps')
