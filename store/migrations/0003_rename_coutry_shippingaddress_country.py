# Generated by Django 3.2.8 on 2021-11-01 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='coutry',
            new_name='country',
        ),
    ]
