# Generated by Django 3.0.3 on 2020-02-14 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_product_toppings'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Product'),
        ),
    ]
