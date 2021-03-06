from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Company
from api.serializers import CompanySerializer


@csrf_exempt
@api_view(["GET", "POST"])
def list_and_create_company(request):
    if request.method == "GET":

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return JsonResponse({"companies": serializer.data})

    elif request.method == "POST":

        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"companies": serializer.data}, status=status.HTTP_201_CREATED)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def get_and_delete_single_company(request, pk):

    try:
        company = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return JsonResponse({"message": "The company does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        company_serializer = CompanySerializer(company)
        return JsonResponse(company_serializer.data)

    elif request.method == "PUT":
        company_serializer = CompanySerializer(company, data=request.data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data)
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        company.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)











