from django.urls import path
from .views import SupplierGenericView, SupplierRUDView

urlpatterns = [
    path('suppliers/', SupplierGenericView.as_view(), name="suppliers_gen_view"),
    path('supplier/<int:id>', SupplierRUDView.as_view(), name="supplier_rud_view")
]