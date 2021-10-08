# Generated by Django 3.1 on 2021-10-08 05:02

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211007_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.JSONField(blank=True, default=products.models.jsonfield_default_value),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.JSONField(blank=True, default=products.models.jsonfield_default_value),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.JSONField(blank=True, default=products.models.jsonfield_default_value),
        ),
    ]
