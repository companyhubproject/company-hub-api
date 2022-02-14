from django.urls import path
from api import views


urlpatterns = [
    path("companies", views.list_and_create_company)
]