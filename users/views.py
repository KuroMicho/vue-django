# django
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
# rest_framework
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
# permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from users.models import User
from .permissions import IsVendorUser
# serializers
from .serializers import CustomTokenObtainPairSerializer, CustomUserSerializer, UserSerializer, CustomStorageUserSerializer

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
                user_serializer = CustomStorageUserSerializer(user)
                return Response({
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'msg': 'Logged in Succesfull'
                }, status=status.HTTP_200_OK)
            return Response({'status':'error', 'msg': 'Username or password invalid'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'status':'error', 'msg': 'User not found'},status=status.HTTP_400_BAD_REQUEST)

@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    response['X-CSRFToken'] = get_token(request)
    return response

# logout refreshing token
class Logout(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

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


# vendor profile
class Profile(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response({'user': serializer.data})

# admin dashboard
class Users(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset =  User.objects.all()

    def get(self, request, *args, **kwargs):
        """
            get users
        """
        queryset = self.get_queryset()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class UserDetail(generics.UpdateAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser,)

    def put(self, request, user_id=None, *args, **kwargs):
        """
            Update user data
        """
        if user_id:
            user = User.objects.get(id=user_id)
            serializer = CustomUserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            return Response({"status": "error", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "msg": "user not found"}, status=status.HTTP_400_BAD_REQUEST)
