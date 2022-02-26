from django.db.models.deletion import CASCADE
from django.db import models


class Administration(models.Model):
    name = models.CharField(max_length=64)
    code = models.IntegerField

    def __str__(self):
        return f"{self.name}, {self.code}"

class Company(models.Model):
    name = models.CharField(max_length=64)
    code = models.IntegerField
    description = models.CharField(max_length=256)
    homepage_url = models.URLField(max_length=256)
    market_value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    administration = models.ForeignKey(Administration, on_delete=CASCADE, related_name="administration")

    def __str__(self):
        return f"{self.name}, {self.code}"

