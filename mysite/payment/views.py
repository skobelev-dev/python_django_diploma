from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from payment.models import Payment
from payment.serializers import PaymentModelSerializer


class PaymentGenericViewSet(CreateModelMixin, GenericViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
