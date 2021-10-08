from django.utils.translation import gettext_lazy as _
from django.db import models

def jsonfield_default_value():  # This is a callable
    return {}  # Any serializable Python obj, e.g. `["A", "B"]` or `{"price": 0}`

class Product(models.Model):
    barcode = models.CharField(blank=False, unique=True, default='123456789', max_length=10)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="media", default='image.jpg', blank=False)
    color = models.JSONField(blank=True, default=jsonfield_default_value)
    material = models.JSONField(blank=True, default=jsonfield_default_value)
    size = models.JSONField(blank=True, default=jsonfield_default_value)
    price = models.FloatField(blank=False, default=0)
    inventory_received = models.IntegerField(blank=True,default=0)
    minimum_required = models.IntegerField(blank=False)
    inventory_onhand = models.IntegerField(blank=True, default=0)
    inventory_shipped = models.IntegerField(blank=True, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name