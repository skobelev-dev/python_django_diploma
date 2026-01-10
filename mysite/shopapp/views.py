from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer

from .models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
