from rest_framework import (
    serializers,
)

from catalogapp.serializers import (
    ProductSerializer,
)
from orders.models import (
    Order,
)




class OrdersModelSerializer(
    serializers.ModelSerializer
):



    class Meta:
        model = Order
        fields = (
            "id",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        )

    id = serializers.IntegerField(
        min_value=1,
        source="pk",
        read_only=True,
    )
    createdAt = serializers.DateTimeField(
        format=r"%Y-%m-%d %H:%M",
        source="created_at",
        read_only=True,
    )
    fullName = serializers.CharField(
        source="user.username"
    )
    email = serializers.EmailField(
        source="user.email"
    )
    phone = serializers.RegexField(
        regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
        source="user.profile.phone",
    )
    products = ProductSerializer(
        many=True,
        error_messages={
            "required": f"This field is required, "
                        f"try to input the field with "
                        f"raw data"
        },
    )
