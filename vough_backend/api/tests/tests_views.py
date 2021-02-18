from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from api.models import Organization
import os

# Create your tests here.

class AccountTests(APITestCase):
    def test_get_organization(self):
        """
        
        """
        data = {'instruct-br', }
        url = reverse('api:orgs-detail', data)        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'login': 'instruct-br',
                                         'name': 'Instruct',
                                          'score': 50}) # Esse score pode mudar.. verificar como deixar isso apenas como int

# Commnet line CTRL K C , CTRL K U 
    # def test_retrieve_organization(self):
    #     """
    #     """
    #     data =  {'instruct-br', }
    #     url = reverse('api:orgs-detail', data)  
    #     urllist = reverse('api:orgs-list')  
    #     response = self.client.get(url, format='json')
    #     responselist = self.client.get(urllist, format='json')
    #     orgs = Organization.objects.filter(
    #         login = 'instruct-br',
    #         name = 'Instruct'
    #     ).exists()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertTrue(orgs)

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


