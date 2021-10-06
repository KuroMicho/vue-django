from rest_framework import serializers
from .models import Product

# PRODUCT
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('name', 'description','color','date_updated','date_created')
        fields = '__all__'