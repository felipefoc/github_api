from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.core import serializers
from api.models import Organization
import os

# Create your tests here.

class OrganizationViewSetTest(APITestCase):
    def test_get_organization(self):
        """
        Teste se o status code retorna 200 e a organização é adicionada
        no banco de dados
        """
        data = {'instruct-br', }
        url = reverse('api:orgs-detail', data)        
        response = self.client.get(url, format='json')
        org = Organization.objects.filter(login='instruct-br').first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'login': org.login,
                                        'name': org.name,
                                        'score': org.score })



    def test_retrieve_organization(self):
        """
        """
        data =  {'instruct-br', }
        url = reverse('api:orgs-detail', data)  
        urllist = reverse('api:orgs-list')  
        response = self.client.get(url, format='json')
        responselist = self.client.get(urllist, format='json')
        orgs = Organization.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


