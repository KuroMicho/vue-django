# rest_framework
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
# permissions
from .permissions import IsVendorUser
from django.contrib.auth import authenticate
# serializers
from .serializers import RegisterSerializer, LoginSerializer

# USER

class AuthUserAPIView(generics.GenericAPIView):

    permission_classes = (IsAuthenticated, IsVendorUser)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({'user': serializer.data})


class RegisterAPIView(generics.GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)

# AUTH VIEWS
# class TokenObtainPairView(TokenViewBase):
#     """
#         Return JWT tokens (access and refresh) for specific user based on username and password.
#     """
#     serializer_class = TokenObtainLifetimeSerializer


# class TokenRefreshView(TokenViewBase):
#     """
#         Renew tokens (access and refresh) with new expire time based on specific user's access token.
#     """
#     serializer_class = TokenRefreshLifetimeSerializer

# class UserView(generics.ListAPIView):
#     # queryset = User.objects.filter(is_active=True)
#     # serializer_class = UserModelSerializer
#     lookup_field = 'username'

#     def get(self, request):
#         queryset = User.objects.all()
#         serializer = UserModelSerializer(queryset, many = True)
#         return Response(serializer.data) 

# class UserLoginView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = UserLoginSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         user, token = serializer.save()
#         data = {
#             'user': UserModelSerializer(user).data,
#             'access_token': token
#         }
#         return Response(data, status=status.HTTP_200_OK)

# class UserSignUpView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = UserSignUpSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         data = UserModelSerializer(user).data
#         return Response(data, status=status.HTTP_201_CREATED)
