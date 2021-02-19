from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.core import serializers
from api.models import Organization
import os

# Create your tests here.


class OrganizationViewSetTest(APITestCase):
    def setUp(self):
        self.organization = ["instruct-br"]

    def test_get_organization(self):
        """
        Teste se o status code retorna 200 e a organização é adicionada
        no banco de dados
        """
        url = reverse("api:orgs-detail", self.organization)
        response = self.client.get(url, format="json")
        org = Organization.objects.filter(login=self.organization[0]).first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {"login": org.login, "name": org.name, "score": org.score}
        )

    def test_list_organizations(self):
        """
        Testa se a organização está na lista de <orgs>
        """
        url_data = reverse("api:orgs-detail", self.organization)
        response_create = self.client.get(
            url_data, format="json"
        )  # Adicionando organização no banco de dados
        url = reverse("api:orgs-list")
        response = self.client.get(url, format="json")  # Lista organizações adicionadas
        orgs = Organization.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), orgs.count()
        )  # Retorna 1 pois somente 1 organização foi adicionada

    def test_del_organization(self):
        """
        Testa se ao deletar a organização é retornado 202 e caso ela não exista, retorne 404
        """
        url = reverse("api:orgs-detail", self.organization)
        response_create = self.client.get(
            url, format="json"
        )  # Adiciona organização no banco de dados
        response = self.client.delete(url)  # Deleta a organização
        response2 = self.client.delete(url)  # Verifica se a organização existe
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
