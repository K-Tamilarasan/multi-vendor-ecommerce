from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsCustomer

from .models import (
    Address,
    Cart,
    CartItem,
    Wishlist,
    WishlistItem,
)

from .serializers import (
    AddressSerializer,
    CartSerializer,
    CartItemSerializer,
    WishlistSerializer,
    WishlistItemSerializer,
)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsCustomer]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsCustomer]


class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = {IsCustomer}


class WishlistItemViewSet(ModelViewSet):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [IsCustomer]