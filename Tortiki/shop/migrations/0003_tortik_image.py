# Generated by Django 4.1.7 on 2023-03-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_tortik_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tortik',
            name='image',
            field=models.ImageField(null=True, upload_to='tortik_img/'),
        ),
    ]
