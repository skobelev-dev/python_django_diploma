from django.contrib import admin

from media.models import Avatar, ProductImage
from orders.models import Order
from payment.models import Payment
from .models import (
    Specifications,
    Tag,
    Category,
    Review,
    Product,
)


@admin.register(Specifications)
class SpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


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
