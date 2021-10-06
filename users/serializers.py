# rest framework
from rest_framework import serializers
# models
from .models import User

# USER
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','is_vendor')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token')

        read_only_fields = ['token']

# AUTH TOKEN
# class TokenObtainLifetimeSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = self.get_token(self.user)
#         data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
#         return data

# class TokenRefreshLifetimeSerializer(TokenRefreshSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         refresh = RefreshToken(attrs['refresh'])
#         data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
#         return data

# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=8, max_length=64)

#     def validate(self, data):
#         user = authenticate(username=data['email'], password=data['password'])
#         if not user:
#             raise serializers.ValidationError('Las credenciales no son validas.')
        
#         self.context['user'] = user
#         return data
    
#     # check here
#     def create(self, data):
#         token, created = Token.objects.get_or_create(user= self.context['user'])
#         return self.context['user'], token.key

# class UserSignUpSerializer(serializers.Serializer):

#     email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
#     username = serializers.CharField(min_length=4, max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])
#     password = serializers.CharField(min_length=8, max_length=64)
#     password_confirmation = serializers.CharField(min_length=8, max_length=64)


#     def validate(self, data):
#         passwd = data['password']
#         passwd_conf = data['password_confirmation']

#         if passwd != passwd_conf:
#             raise serializers.ValidationError("Las contrasenas no coinciden")
#         password_validation.validate_password(passwd)

#         return data
    
#     def create(self, data):
#         data.pop('password_confirmation')
#         # check
#         user = User.objects.create(**data)
#         return user

