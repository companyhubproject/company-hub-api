from rest_framework import serializers
from .models import Administration, Company


class Administration(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"