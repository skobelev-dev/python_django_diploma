from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import ProductSerializer, TagSerializer

from .models import Product, Tag


class TagViewSet(ViewSet):
    """
    Получение списка тегов.
    """
    queryset = Tag.objects.all()

    def list(self, request):
        tags = self.queryset
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
