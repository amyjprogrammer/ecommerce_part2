# Generated by Django 3.1.4 on 2020-12-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='can_backorder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_digital',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='requires_shipping',
            field=models.BooleanField(default=False),
        ),
    ]
