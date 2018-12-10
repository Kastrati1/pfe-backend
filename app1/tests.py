from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase

url = 'http://localhost:8000/app1/'

class UnitTests(APITestCase):
    #############
    #   User    #
    #############
    #POST - expected 201
    def test_inscription_1(self):
        data = {'first_name':'t','last_name':'t','username':'t','password':'t','email':'seb.pau@hotmail.com'}
        client = RequestsClient()
        response = client.post(url+'users/', data)
        assert response.status_code == 201

    def test_inscription_2(self):
        data = {'first_name':'t','last_name':'t','username':'t','email':'seb.pau@hotmail.com'}
        client = RequestsClient()
        response = client.post(url+'users/', data)
        assert response.status_code == 400

    #GET - expected 405
    def test_inscription_3(self):
        client = RequestsClient()
        response = client.get(url+'users/')
        assert response.status_code == 405

    #####################
    #   ProductsByCat   #
    #####################
    #GET - expected 200
    '''
    def test_products_by_cat_1(self):
        client = RequestsClient()
        response = client.get(url+'productsByCat')
        print("cat : ", response.status_code)
        assert response.status_code == 200
    '''

    #POST - expected 405
    def test_products_by_cat_2(self):
        client = RequestsClient()
        response = client.post(url+'productsByCat')
        assert response.status_code == 405

    #########################
    #   GetAllCategories    #
    #########################
    #GET - expected 200
    def test_get_all_categories_1(self):
        client = RequestsClient()
        response = client.get(url+'allCategories')
        assert response.status_code == 200

    #POST - expected 405
    def test_get_all_categories_2(self):
        client = RequestsClient()
        response = client.post(url+'allCategories')
        assert response.status_code == 405