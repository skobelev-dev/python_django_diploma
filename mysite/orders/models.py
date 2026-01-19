from django.contrib.auth.models import User
from django.db import models


class Satus(models.TextChoices):
    ACCEPTED = "accepted"
    NOT_ACCEPTED = "not accepted"


class DeliveryType(models.TextChoices):
    FREE = "free", "Бесплатная доставка"
    PAID = "paid", "Платная доставка"


class PaymentType(models.TextChoices):
    ONLINE = "online", "Онлайн"
    CASH = "cash", "Наличными"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # Как я полагаю: имя, почта и телефон - пользователя совершившего заказ
    user = models.ForeignKey(User, related_name="orders", on_delete=models.DO_NOTHING)
    deliveryType = models.CharField(
        max_length=20, choices=DeliveryType.choices, default=DeliveryType.FREE
    )
    paymentType = models.CharField(
        max_length=20, choices=PaymentType.choices, default=PaymentType.ONLINE
    )
    totalCost = models.DecimalField(max_digits=10**9, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=Satus.choices, default=Satus.ACCEPTED
    )
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=70)
    products = models.ManyToManyField(Product, related_name="orders")

    def __str__(self):
        return f"Order(pk={self.pk}, created_at={self.created_at!r})"
