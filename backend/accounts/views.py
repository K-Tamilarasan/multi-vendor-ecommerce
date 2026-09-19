from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import User, SellerProfile
from .serializers import UserSerializer, SellerProfileSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SellerProfileViewSet(ModelViewSet):
    queryset = SellerProfile.objects.all()
    serializer_class = SellerProfileSerializer