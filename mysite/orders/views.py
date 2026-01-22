from django.shortcuts import render
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Order
from .serializers import OrdersModelSerializer


class OrderGenericViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    serializer_class = OrdersModelSerializer
    queryset = Order.objects.prefetch_related("products", "user__profile")
