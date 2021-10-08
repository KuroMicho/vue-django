# Generated by Django 3.1 on 2021-10-08 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(default='123456789', max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='image.jpg', upload_to='media')),
                ('color', models.JSONField(blank=True)),
                ('material', models.JSONField(blank=True)),
                ('size', models.JSONField(blank=True)),
                ('price', models.FloatField(default=0)),
                ('inventory_received', models.IntegerField(default=0)),
                ('minimum_required', models.IntegerField()),
                ('inventory_onhand', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('address', models.TextField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
                ('number_purchases', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.supplier')),
            ],
        ),
    ]
