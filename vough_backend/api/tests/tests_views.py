from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from django.core import serializers
from api.models import Organization
import json
import os


class OrganizationViewSetTest(APITestCase):
    def setUp(self):
        self.organization = ["instruct-br"]

    def test_get_organization(self):
        """
        Teste se a organização adicionada no banco de dados
        """
        url = reverse("api:orgs-detail", self.organization)
        response = self.client.get(url, format="json")
        org = Organization.objects.filter(login=self.organization[0]).first()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, {"login": org.login, "name": org.name, "score": org.score}
        )

    def test_get_organization_not_exists(self):
        """
        Teste se a organização existe no github
        """
        url = reverse("api:orgs-detail", ["notExistenceOrg"])
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_organizations(self):
        """
        Testa se a organização está na lista de <orgs>
        """
        org = Organization.objects.create(login="org1", name="OrgName", score=30)
        org2 = Organization.objects.create(login="org2", name="OrgName2", score=40)

        url = reverse("api:orgs-list")
        response = self.client.get(url, format="json")  # Lista organizações adicionadas
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            [
                {"login": org2.login, "name": org2.name, "score": org2.score},
                {"login": org.login, "name": org.name, "score": org.score},
            ],
        )

    def test_del_organization(self):
        """
        Testa se ao deletar a organização é retornado 202
        """
        org = Organization.objects.create(login="org1", name="OrgName", score=30)
        url = reverse("api:orgs-detail", [org.login])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Organization.objects.filter(pk=org.pk).exists())

    def test_del_organization_not_exist(self):
        """
        Testa se caso a organização não exista, retorne 404
        """
        url = reverse("api:orgs-detail", ["organization"])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
