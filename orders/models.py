from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    TOPPINGS_NUMBER = [
        (ONE, "One"),
        (TWO, "Two"),
        (THREE, "Three"),
        (ZERO, "Not available"),
    ]
    name = models.CharField(max_length=64)
    number_of_toppings = models.IntegerField(choices=TOPPINGS_NUMBER, default=ZERO)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # price ? FK or value?

    def __str__(self):
        name = " ".join(
            [
                str(self.category),
                self.name,
                str(self.number_of_toppings),
                "topping" if self.number_of_toppings == 1 else "toppings",
            ]
        )
        return name


class Price(models.Model):
    SMALL = "S"
    LARGE = "L"
    PRICE_TYPE = [(SMALL, "Small"), (LARGE, "Large")]
    name = models.CharField(max_length=1, choices=PRICE_TYPE, default=SMALL)
    value = models.FloatField()

    def __str__(self):
        return f"{self.name} = {self.value}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
