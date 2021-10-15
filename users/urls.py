from django.urls import path
from rest_framework_simplejwt.views import (TokenRefreshView)
from users import views

urlpatterns = [
    path('user/', views.Register.as_view({'post': 'create'})),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('users/', views.AuthUserAPIView.as_view()),
]