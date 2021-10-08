# django
from django.db.models import F
from django.utils.translation import gettext_lazy as _
# rest_framework
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

# models
from .models import Product, Purchase
# serializers
from .serializers import PurchaseSerializer

# Create your views here.


# PURCHASE VIEWS

class PurchasesRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    # Crear Modal para pasar id en url.

    def get(self, request, product_id, *args, **kwargs):
        """
            Get all purchases by product
        """
        queryset = Purchase.objects.filter(product=product_id).all()
        serializer = PurchaseSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class PurchaseCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, product_id, *args, **kwargs):
        """
            Add a purchase according to product id
        """
        query =  Product.objects.filter(id=product_id)
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("UPDATED")
            purchase = Purchase.objects.latest('id')
            query.update(inventory_received= F('inventory_received') + purchase.number_purchases)
            query.update(inventory_onhand= F('inventory_onhand') + purchase.number_purchases)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)