from django.contrib import admin

# Register your models here.
from .models import Food, Menu, Price

admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Price)
