# Generated by Django 3.0.3 on 2020-02-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200214_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='products', to='orders.Product'),
        ),
    ]
