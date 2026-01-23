# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet

from reviews.serializers import ReviewSerializer
from .serializers import ProductSerializer, BasketModelSerializer
from rest_framework.response import Response
from .models import Product, Tag, Basket
from .serializers import TagSerializer


def get_products_ids():
    return [obj.pk for obj in Product.objects.values_list("pk", flat=True)]


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

    @action(methods=["get"], url_name="get-products-ids", detail=False)
    def ids(self):
        return Response(data={"products ids": get_products_ids()}, status=200)


class TagViewSet(ViewSet):
    """
    Получение списка тегов.
    """

    queryset = Tag.objects.all()

    def list(self, request):
        tags = self.queryset
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class BasketViewSet(ViewSet):

    default_serializer = BasketModelSerializer
    queryset = Basket.objects.all()

    def list(self, request: Request):

        if request.user.is_authenticated:
            objects = Basket.objects.filter(user=request.user).prefetch_related("product__category")
            serialized = BasketModelSerializer(objects, many=True)
            return Response(serialized.data)
        return Response(data={"msg": "you are not authenticated"})


