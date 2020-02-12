from django.contrib import admin

# Register your models here.
from .models import Category, Price, Product, Topping

admin.site.register(Category)
admin.site.register(Price)
admin.site.register(Product)
admin.site.register(Topping)
