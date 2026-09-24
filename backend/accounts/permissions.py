
from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'ADMIN'
        )

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'SELLER'
        )

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        # return False
        return (
            request.user.is_authenticated
            and request.user.role == 'CUSTOMER'
        )

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and (
                obj == request.user
                or request.user.role == 'ADMIN'
            )
        )

class IsSellerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role == 'ADMIN':
            return True

        if request.user.role != 'SELLER':
            return False

        # return obj.seller.user == request.user

        return (
            hasattr(request.user, 'seller_profile')
            and request.user.seller_profile.status == 'APPROVED'
        )

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'ADMIN':
            return True

        return obj.seller.user == request.user