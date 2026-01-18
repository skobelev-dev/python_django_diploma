from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Payment(models.Model):
    number = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(10**15 - 1, "15 цифр"),
        ],
    )
    name = models.CharField(max_length=35)
    month = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(12),
        ]
    )
    year = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(2000, "Год от 2000"),
            MaxValueValidator(2099, "Год до 2099"),
        ],
    )
    code = models.CharField(
        max_length=3,
        validators=[
            RegexValidator(
                r"^[0-9]{3}$",
            )
        ],
    )

    def __str__(self):
        return f"Payment(pk={self.pk}, name={self.name!r})"
