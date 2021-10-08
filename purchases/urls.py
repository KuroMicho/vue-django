from django.urls import path
from .views import PurchaseCreateView, PurchasesRetrieveView

urlpatterns = [
    path('product/<int:product_id>/purchase/', PurchaseCreateView.as_view(), name='purchases_create_view'),
    path('product/<int:product_id>/purchases/', PurchasesRetrieveView.as_view(), name="purchases_all_product_view"),
]