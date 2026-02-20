from django.urls import path
from .views import test_api, recommend, list_requests

urlpatterns = [
    path("test/", test_api, name="test_api"),
    path("recommend/", recommend, name="recommend"),
    path("requests/", list_requests, name="list_requests"),
]