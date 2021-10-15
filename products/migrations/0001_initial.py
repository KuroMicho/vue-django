# Generated by Django 3.2.8 on 2021-10-14 19:47

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(default='123456789', max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.URLField()),
                ('color', models.JSONField(blank=True, default=products.models.jsonfield_default_value)),
                ('material', models.JSONField(blank=True, default=products.models.jsonfield_default_value)),
                ('size', models.JSONField(blank=True, default=products.models.jsonfield_default_value)),
                ('price', models.FloatField(default=0)),
                ('inventory_received', models.IntegerField(blank=True, default=0)),
                ('minimum_required', models.IntegerField()),
                ('inventory_onhand', models.IntegerField(blank=True, default=0)),
                ('inventory_shipped', models.IntegerField(blank=True, default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
