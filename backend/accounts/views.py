from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import User, SellerProfile
from .serializers import UserSerializer, SellerProfileSerializer
from .permissions import IsOwnerOrAdmin
from accounts.permissions import IsAdmin

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.role == 'ADMIN':
                return User.objects.all()

            return User.objects.filter(
                user_id=self.request.user.user_id
            )
        return User.objects.none()

    def get_permissions(self):
        if self.action == 'create':
            return []

        return [IsOwnerOrAdmin()]


class SellerProfileViewSet(ModelViewSet):
    # queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return SellerProfile.objects.none()

        if self.request.user.role == 'ADMIN':
            return SellerProfile.objects.all()

        return SellerProfile.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]

        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user

        if user.role != 'SELLER':
            raise PermissionDenied("Only sellers can create a seller profile.")

        if SellerProfile.objects.filter(user=user).exists():
            raise PermissionDenied("Seller profile already exists.")

        serializer.save(user=user,status='PENDING')

    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAdmin]
    )
    def approve(self, request, pk=None):
        seller_profile = self.get_object()

        seller_profile.status = 'APPROVED'
        seller_profile.save(update_fields=['status','updated_at'])

        return Response(
            {
                'message': 'Seller approved successfully.',
                'status': seller_profile.status
            }
        )

    @action(
        detail=True,
        methods=['patch'],
        permission_classes=[IsAdmin]
    )
    def reject(self, request, pk=None):
        seller_profile = self.get_object()

        seller_profile.status = 'REJECTED'
        seller_profile.save(update_fields=['status','updated_at'])

        return Response(
            {
                'message': 'Seller rejected successfully.',
                'status': seller_profile.status
            }
        )