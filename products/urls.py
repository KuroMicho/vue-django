from django.urls import path
from .views import ProductsView, ProductView

urlpatterns = [
    path('products/', ProductsView.as_view(), name="products_view"),
    path('products/<int:id>', ProductView.as_view(), name="product_view"),
]