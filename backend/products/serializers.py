from rest_framework import serializers
from .models import Category, Product, ProductImage, Inventory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'image',
            'is_active',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'seller',
            'category',
            'name',
            'description',
            'price',
            'discount_price',
            'sku',
            'brand',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'seller',
            'created_at',
            'updated_at',
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [
            'id',
            'product',
            'image',
            'is_primary',
            'display_order',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = [
            'id',
            'product',
            'quantity',
            'reserved_quantity',
            'low_stock_threshold',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'updated_at',
        ]