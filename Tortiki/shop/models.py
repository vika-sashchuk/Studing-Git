from django.db import models

# Create your models here.

SHOP_TYPE_CHOICES = [
    ('store', 'Store'),
    ('delivery', 'Delivery'),
    ('stock', 'Stock')
    ]

TORTIK_TYPE_CHOICES = [
    ('biscuit ', 'Biscuit'),
    ('alicante', 'Alicante'),
    ('banana', 'Banana'),
    ('kyiv', 'Kyiv')
    ]


class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    shop_type = models.CharField(choices=SHOP_TYPE_CHOICES, max_length=50)

    def __str__(self) -> str:
        return self.name


class Tortik(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tortik_img/', null=True)
    tortik_type = models.CharField(choices=TORTIK_TYPE_CHOICES, max_length=50)
    description = models.TextField()
    weight = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.name
