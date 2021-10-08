from django.urls import path
from .views import SaleCreateView, SalesRetrieveView

urlpatterns = [
    path('product/<int:product_id>/sale/', SaleCreateView.as_view(), name="sale_create_view"),
    # sales by product
    path('product/<int:product_id>/sales/', SalesRetrieveView.as_view(), name="sales_all_product_view"),
    # all sales
    # path('sales/', SaleCreateView.as_view(), name="sale_create_view")
]