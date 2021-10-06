from django.db import models

# Create your models here.

class Product(models.Model):
    barcode = models.IntegerField(blank=False, unique=True)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to="media", default='image.jpg', blank=False)
    color = models.JSONField()
    material = models.JSONField()
    size = models.JSONField()
    price = models.FloatField(blank=False)
    inventory_received = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name

# TO DO LATER 

# class Supplier(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20, unique=True)
#     address = models.TextField()
#     location = models.CharField(max_length=100)
    

# class Purchase(models.Model):
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     date_purchased = models.DateTimeField(auto_now_add=True)
#     number_purchases = models.IntegerField()
   
    def __str__(self) -> str:
        return self.name