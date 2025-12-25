from django.urls import path
from .views import test_view

app_name = "shop"

urlpatterns = [
    path("test-view/", test_view)
]
