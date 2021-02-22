from django.db import models
from rest_framework.mixins import CreateModelMixin


class Organization(models.Model):
    login = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    score = models.IntegerField()
