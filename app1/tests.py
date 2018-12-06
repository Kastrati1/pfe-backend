from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .models import User


class UserTests(APITestCase):

    def test_create_post_request(self):
        
        factory = APIRequestFactory()
        request = factory.post('/inscription/',{
            'first_name': 'k',
            'last_name': 'xhakol',
            'email': 'kxhakol@gmail.com',
            'login': 'kxhakol',
            'password': '111'}, format='json')

    
    def test_create_User(self):


        data = {'name': 'DabApps'}
        response = self.client.post('/inscription/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        #self.assertEqual(User.objects.count(), 1)
        #self.assertEqual(User.objects.get().name, 'DabApps')
        
    
    def test_create_User1(self):

        data = {'first_name': 'k',
                'last_name': 'xhakol',
                'email': 'kxhakol@gmail.com',
                'login': 'kxhakol',
                'password': '111'}
        reponse = self.client.post('/inscription/', data, format='json')
        self.assertEqual(reponse.status_code, status.HTTP_404_NOT_FOUND)

