from django.contrib import admin

from .models import (
    Specifications,
    Tag,
    Category,
    Product,
)


@admin.register(Specifications)
class SpecificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
