from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    products = models.ManyToManyField("Product", related_name="products", blank=True)

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
    prices = models.ManyToManyField("Price", related_name="prices", blank=True)
    toppings = models.ManyToManyField("Topping", related_name="toppings", blank=True)

    def __str__(self):
        # with toppings: {', '.join([topping.name for topping in self.toppings.all()])}.
        return f"{self.name} Prices: {', '.join(['='.join((price.name, str(price.value))) for price in self.prices.all()])}"


class Price(models.Model):
    SMALL = "S"
    LARGE = "L"
    PRICE_TYPE = [(SMALL, "Small"), (LARGE, "Large")]
    name = models.CharField(max_length=1, choices=PRICE_TYPE, default=SMALL)
    value = models.FloatField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, default=None
    )

    def __str__(self):
        return f"{self.name} = {self.value}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
