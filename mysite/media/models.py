from django.contrib.auth.models import User
from django.db import models


def product_images_directory_path(instance: "ProductImage", filename: str) -> str:
    pk: "Product.pk" = instance.product.pk
    return f"products/product_{pk}/{filename}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="images"
    )

    image = models.ImageField(upload_to=product_images_directory_path)

    alt = models.CharField(max_length=50)

    def __str__(self):
        return f"ProductImage(pk={self.pk}, alt={self.alt!r})"


def gen_path_to_avatar(instance: "Avatar", filename: str) -> str:
    return f"avatars/{instance.pk}/{filename}"


class Avatar(models.Model):
    image = models.ImageField(upload_to=gen_path_to_avatar, null=True, blank=True)
    alt = models.CharField(max_length=255, blank=True)

    user = models.OneToOneField(
        User, related_name="avatar", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"Avatar(pk={self.pk}, alt={self.alt!r})"
