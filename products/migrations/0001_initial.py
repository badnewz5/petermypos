# Generated by Django 4.1.7 on 2023-02-20 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('branches', '0001_initial'),
        ('suppliers', '0002_rename_primary_phone_supplier_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('manufacturer', models.CharField(blank=True, max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sku_code', models.CharField(max_length=25, unique=True)),
                ('product_image', models.ImageField(blank=True, upload_to='product_images')),
                ('quantity', models.IntegerField(default=0, help_text='Quantity in stock')),
                ('buying_price', models.FloatField(default=0.0)),
                ('retail_price', models.FloatField(default=0.0)),
                ('wholesale_price', models.FloatField(default=0.0)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('date_received', models.DateTimeField(blank=True, null=True)),
                ('received', models.BooleanField(default=False)),
                ('value', models.FloatField(default=0.0)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('transfer_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_from', to='branches.branch')),
                ('transfer_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_to', to='branches.branch')),
            ],
            options={
                'permissions': [('receive_transfer', 'Can receive transfer')],
            },
        ),
        migrations.CreateModel(
            name='TransferProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('unit_cost', models.FloatField(default=0.0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.transfer')),
            ],
        ),
        migrations.CreateModel(
            name='BranchProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0.0)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='branches.branch')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]
