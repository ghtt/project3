# Generated by Django 3.0.3 on 2020-02-14 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_topping_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='product',
        ),
    ]
