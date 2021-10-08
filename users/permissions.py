from rest_framework.permissions import BasePermission

from .models import User

class IsVendorUser(BasePermission):
    def has_permission(self, request, view):
        try :
            if User.objects.get(email = request.user, is_vendor=True):
                return True
        except User.DoesNotExist:
            return False