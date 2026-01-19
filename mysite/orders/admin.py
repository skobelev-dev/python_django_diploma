from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "user",
        "deliveryType",
        "paymentType",
        "totalCost",
        "status",
        "city",
        "address",
    )