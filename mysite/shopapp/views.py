from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.viewsets import ModelViewSet

from .models import Product



# class ProductViewSet(ModelViewSet):
# 	queryset = Product
# 	serializer_class = ProductSerializer