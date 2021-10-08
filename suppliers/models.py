from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False,unique=True)
    phone_number = models.CharField(max_length=20, blank=False, unique=True)
    address = models.TextField()
    location = models.CharField(max_length=50)