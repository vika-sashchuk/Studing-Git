from django.db import models

# Create your models here.

SHOP_TYPE_CHOICES = [
    ('store', 'Store'),
    ('delivery', 'Delivery'),
    ('stock', 'Stock')
    ]

PRODUCT_TYPE_CHOICES = [
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


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_img/', null=True)
    product_type = models.CharField(choices=PRODUCT_TYPE_CHOICES, max_length=50)
    description = models.TextField()
    weight = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self) -> str:
        return self.name
