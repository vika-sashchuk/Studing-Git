from django.contrib import admin
from shop.models import Shop, Tortik

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(Tortik)
class TortikAdmin(admin.ModelAdmin):
    pass

# Register your models here.
