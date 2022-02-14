from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Company
from api.serializers import CompaniesSerializer


# @api_view(["GET","POST"])
# @csrf_exempt
# def list_and_create_costumer(request):
#     if request.method == "GET":
#         return HttpResponse(status=200)
#     elif request.method == "POST":
#         return HttpResponse(status=201)
#     else:
#         return HttpResponse(status=405)


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

    







        # data = JSONParser().parse(stream=request,media_type="application/json")
        # serializer = CompaniesSerializer(data=data)
        # if serializer.is_valid():
        #     company = serializer.save()
        #     response = HttpResponse(status=201)
        #     response["Location"] = "/api/companies/" + str(company.id)

        #     return response
    










