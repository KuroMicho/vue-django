# Generated by Django 3.1 on 2021-10-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20211007_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inventory_onhand',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]