from rest_framework import serializers

from payment.models import Payment


class PaymentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "number", "name", "month", "year", "code"