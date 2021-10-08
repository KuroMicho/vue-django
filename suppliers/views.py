# django
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
# rest_framework
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
# models
from .models import Supplier
# serializers
from .serializers import SupplierSerializer

# Create your views here.


# PROVEEDOR VISTAS

class SupplierGenericView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    queryset =  Supplier.objects.all()

    def post(self, request, *args, **kwargs):
        """
            Add a supplier
        """
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        """
            Get all suppliers
        """
        queryset = self.get_queryset()
        serializer = SupplierSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class SupplierRUDView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None, *args, **kwargs):
        """
            Get one supplier
        """
        if id:
            supplier = Supplier.objects.get(id=id)
            serializer = SupplierSerializer(supplier)
            return Response(serializer.data)

    def put(self, request, id=None, *args, **kwargs):
        """
            Update supplier data
        """
        if id:
            supplier = Supplier.objects.get(id=id)
            serializer = SupplierSerializer(supplier, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        """
            Delete supplier
        """
        supplier = get_object_or_404(Supplier, id=id)
        supplier.delete()
        return Response({"status": "success", "data": "Supplier Deleted"})