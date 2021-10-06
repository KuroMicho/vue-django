# from django.shortcuts import render
# rest_framework
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# models
from .models import Product
# permisioon
from users.permissions import IsVendorUser
# serializers
from .serializers import ProductSerializer

# Create your views here.


# PRODUCT VIEWS

# GET ALL PRODUCTS
class ProductsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsVendorUser)
    queryset =  Product.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

# GET ONE PRODUCT (GET, PUT, PATCH)
class ProductView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request, id=None, *args, **kwargs):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
    
    def patch(self, request, id=None, *args, **kwargs):
        if id:
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})