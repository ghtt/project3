# Generated by Django 3.0.3 on 2020-02-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200214_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Topping'),
        ),
    ]