# Generated by Django 4.1.5 on 2023-02-24 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tax',
        ),
    ]