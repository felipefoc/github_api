from rest_framework import viewsets, status
from rest_framework.views import Response

from .serializers import OrganizationSerializer
from .models import Organization

from api import models, serializers
from api.integrations.github import GithubApi


# TODOS:
# 1 - Buscar organização pelo login através da API do Github ✓
# 2 - Armazenar os dados atualizados da organização no banco ✓
# 3 - Retornar corretamente os dados da organização ✓
# 4 - Retornar os dados de organizações ordenados pelo score na listagem da API ✓


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all().order_by("-score")
    serializer_class = OrganizationSerializer
    lookup_field = "login"

    def retrieve(self, request, login=None):
        api = GithubApi()
        data = api.get_organization(login)

        public_members = api.get_organization_public_members(login)
        try:
            organization = {
                "login": data["login"],
                "name": data["name"],
                "score": data["public_repos"] + public_members,
            }
        except KeyError:
            message = {"message": "Not Found"}
            return Response(data=message, status=status.HTTP_404_NOT_FOUND)

        serializer = OrganizationSerializer(data=organization)

        if serializer.is_valid():
            serializer.save()

        return Response(organization)
