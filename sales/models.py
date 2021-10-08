from django.db import models
from products.models import Product
# Create your models here.

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_shipments = models.IntegerField(blank=False)
    date_shipped = models.DateTimeField(auto_now_add=True)