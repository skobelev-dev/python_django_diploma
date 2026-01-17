# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.response import Response
from .models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(
        detail=True,
        methods=[
            "post",
        ],
        url_path="review",
        serializer_class=ReviewSerializer,
    )
    def review(self, request, pk=None):
        print(request.data)
        user = self.request.user
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = serializer.save(author=user)
        return Response(ReviewSerializer(review).data, status=201)
