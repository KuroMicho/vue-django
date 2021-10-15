# django
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
# rest_framework
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
# models
from .models import Product
# permissions
from users.permissions import IsVendorUser
# serializers
from .serializers import ProductSerializer

# PRODUCT VIEWS

class ProductCreateView(generics.CreateAPIView):

    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# GET ALL PRODUCTS
class ProductsRetrieveView(generics.RetrieveAPIView):
    # permission_classes = (IsAuthenticated, IsVendorUser)
    queryset =  Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

# GET ONE PRODUCT (GET, PUT, PATCH)
class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None, *args, **kwargs):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    def put(self, request, id=None, *args, **kwargs):
        if id:
            product = Product.objects.get(id=id)
            if request.data['inventory_onhand'] < product.minimum_required:
                return Response({"status": "inventory on hand is not allowed to be less than minimum required"}, status=status.HTTP_400_BAD_REQUEST)
            if request.data['inventory_received'] != product.inventory_received:
                return Response({"status": "update inventory received is not allowed such as this way"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer = ProductSerializer(product, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    # to update color, size, material
    def patch(self, request, id=None, *args, **kwargs):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})

    def delete(self, request, id=None):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return Response({"status": "success", "data": "Product Deleted"})