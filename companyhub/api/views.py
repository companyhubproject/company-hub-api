from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Company
from api.serializers import CompaniesSerializer


@csrf_exempt
@api_view(["GET", "POST"])
def list_and_create_company(request):
    if request.method == "GET":

        companies = Company.objects.all()
        serializer = CompaniesSerializer(companies, many=True)

        return JsonResponse({"companies": serializer.data})

    elif request.method == "POST":

        serializer = CompaniesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"companies": serializer.data}, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def get_and_delete_single_company(request, pk):
        
    try:
        company = Company.objects.get(pk)
    except Company.DoesNotExist:
        return JsonResponse({"message": "The company does not exist"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        company_serializer = CompaniesSerializer(company)
        return JsonResponse(company_serializer.data)

    elif request.method == "PUT":
        company_data = JSONParser().parse(request)
        company_serializer = CompaniesSerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data)
        return JsonResponse(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # elif request.method == "PUT":

    #     serializer = CompaniesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({"companies": serializer.data},status=status.HTTP_201_CREATED)
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











