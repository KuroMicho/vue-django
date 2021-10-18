from rest_framework import serializers
from purchases.models import Purchase
from suppliers.serializers import SupplierSerializer

# COMPRA
class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields= '__all__'

    # def to_representation(self, instance):
    #     self.fields['supplier'] =  SupplierSerializer(read_only=True)
    #     return super(PurchaseSerializer, self).to_representation(instance)