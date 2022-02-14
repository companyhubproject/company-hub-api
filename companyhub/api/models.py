from unittest.util import _MAX_LENGTH
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    homepage_url = models.URLField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)