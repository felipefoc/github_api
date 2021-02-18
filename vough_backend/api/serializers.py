from rest_framework import serializers
from .models import Organization

from api import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

