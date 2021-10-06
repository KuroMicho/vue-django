from django.urls import path
from .views import AuthUserAPIView,RegisterAPIView,LoginAPIView

urlpatterns = [
    path('users/', AuthUserAPIView.as_view(), name="users"),
    path('register/', RegisterAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    # path('api-token/', TokenObtainPairView.as_view()),
    # path('api-token-refresh/', TokenRefreshView.as_view()),
]