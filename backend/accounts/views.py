from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import User, SellerProfile
from .serializers import UserSerializer, SellerProfileSerializer
from .permissions import IsOwnerOrAdmin



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
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer