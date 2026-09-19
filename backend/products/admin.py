
# Register your models here.

from django.contrib import admin
from .models import Category, Product, ProductImage, Inventory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'seller',
        'category',
        'price',
        'discount_price',
        'sku',
        'is_active',
        'created_at',
    )

    list_filter = (
        'category',
        'is_active',
    )

    search_fields = (
        'name',
        'sku',
        'brand',
        'seller__store_name',
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'is_primary',
        'display_order',
        'created_at',
    )

    list_filter = (
        'is_primary',
    )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'quantity',
        'reserved_quantity',
        'low_stock_threshold',
        'updated_at',
    )

    list_filter = (
        'quantity',
    )

    search_fields = (
        'product__name',
        'product__sku',
    )