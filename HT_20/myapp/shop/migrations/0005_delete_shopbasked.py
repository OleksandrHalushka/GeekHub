# Generated by Django 4.0.2 on 2022-02-15 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShopBasked',
        ),
    ]
