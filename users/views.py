# django
from django.contrib.auth import authenticate
# rest_framework
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
# permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsVendorUser
# models
from users.models import User
# serializers
from .serializers import CustomTokenObtainPairSerializer, CustomUserSerializer, UserSerializer

# USER

# registration
class Register(viewsets.GenericViewSet):

    serializer_class = UserSerializer
    def create(self,request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"msg": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response({"msg": "Error found", "error": user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# login
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'msg': 'Logged in Succesfull'
                }, status=status.HTTP_200_OK)
            return Response({'status':'error', 'msg': 'Username or password invalid'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'error', 'msg': 'Username or password invalid'},status=status.HTTP_400_BAD_REQUEST)

# logout refreshing token
class Logout(generics.GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'status':'success', 'msg': 'User logout successfull'},status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"status": "error", "msg": "invalid refresh token or expired"}, status=status.HTTP_400_BAD_REQUEST)
        # user = User.objects.filter(id=request.data.get('user', 0))
        # if user.exists():
        #     RefreshToken.for_user(user.first())
        #     # token = RefreshToken(request.data.get('refresh'))
        #     # token.blacklist()
            # return Response({'status':'success', 'msg': 'User logout successfull'},status=status.HTTP_205_RESET_CONTENT)
        # return Response({'status':'error', 'msg': 'User not exist'},status=status.HTTP_400_BAD_REQUEST)


class AuthUserAPIView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data})
