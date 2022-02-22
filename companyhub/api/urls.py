from django.urls import path, re_path
from api import views


urlpatterns = [
    path("companies", views.list_and_create_company),
    path("companies/<int:pk>", views.get_and_delete_single_company)
]