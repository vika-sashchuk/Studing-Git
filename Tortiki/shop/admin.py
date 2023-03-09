from django.contrib import admin
from shop.models import Shop, Tortik

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'shop_type']

@admin.register(Tortik)
class TortikAdmin(admin.ModelAdmin):
    list_display = ('name', 'tortik_type', 'weight')

# Register your models here.
