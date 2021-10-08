from suppliers.models import Supplier
from rest_framework import serializers

# PROVEEDOR
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'