from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Price(models.Model):
    price_type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.price_type}"


class Food(models.Model):
    food_type = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.food_type}"


class Menu(models.Model):
    food_type = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    price_type = models.ForeignKey(to=Price, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.food_type} {self.name} - {self.price_type} {self.price}"
