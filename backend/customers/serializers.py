from rest_framework import serializers
from .models import Address, Cart, CartItem, Wishlist, WishlistItem


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'user',
            'address_type',
            'full_name',
            'phone',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'postal_code',
            'country',
            'is_default',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = [
            'id',
            'cart',
            'product',
            'quantity',
            'added_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'added_at',
            'updated_at',
        ]


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
            'updated_at',
        ]


class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = [
            'id',
            'wishlist',
            'product',
            'added_at',
        ]
        read_only_fields = [
            'id',
            'added_at',
        ]