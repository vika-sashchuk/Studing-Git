# Generated by Django 4.1.7 on 2023-03-09 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, 
                                           primary_key=True, 
                                           serialize=False, 
                                           verbose_name='ID')
                                           ),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('shop_type', models.CharField(choices=[('store', 'store'), 
                                                        ('delivery', 'delivery'), 
                                                        ('stock', 'stock')], max_length=50)
                                                        ),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, 
                                           serialize=False, verbose_name='ID')
                                           ),
                ('product_type', models.CharField(choices=[('biscuit ', 'biscuit'), 
                                                           ('alicante', 'alicante'), 
                                                           ('banana', 'banana'), 
                                                           ('kyiv', 'kyiv')], 
                                                           max_length=50)
                                                           ),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
