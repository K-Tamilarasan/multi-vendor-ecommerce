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
    # queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartViewSet(ModelViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemViewSet(ModelViewSet):
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart = serializer.validated_data['cart']

        if cart.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You can only add items to your own cart.")
        serializer.save()


class WishlistViewSet(ModelViewSet):
    # queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WishlistItemViewSet(ModelViewSet):
    # queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        return WishlistItem.objects.filter(wishlist__user=self.request.user)

    def perform_create(self, serializer):
        wishlist = serializer.validated_data['wishlist']

        if wishlist.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You can only add items to your own wishlist.")
        serializer.save()