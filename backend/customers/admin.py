
# Register your models here.

from django.contrib import admin
from .models import Address, Cart, CartItem, Wishlist, WishlistItem


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'user',
        'address_type',
        'city',
        'state',
        'postal_code',
        'is_default',
    )

    list_filter = (
        'address_type',
        'is_default',
        'state',
    )

    search_fields = (
        'full_name',
        'phone',
        'city',
        'postal_code',
        'user__email',
    )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'user__email',
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'cart',
        'product',
        'quantity',
        'added_at',
    )

    search_fields = (
        'cart__user__email',
        'product__name',
        'product__sku',
    )


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'user__email',
    )


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = (
        'wishlist',
        'product',
        'added_at',
    )

    search_fields = (
        'wishlist__user__email',
        'product__name',
        'product__sku',
    )