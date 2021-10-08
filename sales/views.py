# django
from django.db.models import F
# rest framework
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
# permission
from users.permissions import IsVendorUser
# models
from products.models import Product
from .models import Sale
# serializers
from sales.serializers import SaleSerializer

# Create your views here.

class SaleCreateView(generics.CreateAPIView):
    
    permission_classes = (IsAuthenticated,IsVendorUser)

    def post(self, request, product_id, *args, **kwargs):
        """
            Make a sale according to product id
        """
        query =  Product.objects.filter(id=product_id)
        no_pass_threshold = int(query.first().inventory_onhand) - int(request.data['number_shipments']) >= int(query.first().minimum_required)
        if no_pass_threshold:
            serializer = SaleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                print("SOLD")
                sale = Sale.objects.latest('id')
                query.update(inventory_shipped=F('inventory_shipped') + sale.number_shipments)
                query.update(inventory_onhand=F('inventory_onhand') - sale.number_shipments)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "You are not allowed to sale more products, minimum required reaching"}, status=status.HTTP_400_BAD_REQUEST)

class SalesRetrieveView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsVendorUser)

    def get(self, request, product_id, *args, **kwargs):
        """
            Get all sales by product
        """
        queryset = Sale.objects.filter(product=product_id).all()
        serializer = SaleSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
