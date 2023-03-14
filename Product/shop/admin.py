from django.contrib import admin
from shop.models import Shop, Product

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'shop_type']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'product_type', 'weight', 'description', )

# Register your models here.
