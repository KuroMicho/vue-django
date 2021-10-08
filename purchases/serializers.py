from rest_framework import serializers
from purchases.models import Purchase


# COMPRA
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields= '__all__'