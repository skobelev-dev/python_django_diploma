from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models


class Review(models.Model):
    author = models.ForeignKey(
        User, related_name="reviews", on_delete=models.DO_NOTHING
    )
    text = models.TextField(max_length=880)
    rate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5, "5-ти бальная система"),
        ],
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review(pk={self.pk}, author={self.author!r})"
