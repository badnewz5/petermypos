# Generated by Django 4.1.7 on 2023-02-26 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tax',
        ),
    ]