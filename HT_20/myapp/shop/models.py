from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    TECHNIC = "TC"
    MOBILE = "MB"
    TELEVISION = "TV"
    CATEGORY_CHOICES = [
        (TECHNIC, 'Technic'),
        (MOBILE, 'Mobile'),
        (TELEVISION, 'Television')

    ]
    manufactured = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    remainder = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    price = models.FloatField(default=0)
    class Meta:
        verbose_name_plural = 'Products'
