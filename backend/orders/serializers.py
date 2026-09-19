from rest_framework import serializers
from .models import (
    Order,
    SellerOrder,
    OrderItem,
    Payment,
    Review,
    OrderStatusHistory,
)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'address',
            'order_number',
            'subtotal',
            'shipping_fee',
            'discount_amount',
            'total_amount',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'order_number',
            'created_at',
            'updated_at',
        ]


class SellerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerOrder
        fields = [
            'id',
            'order',
            'seller',
            'subtotal',
            'shipping_fee',
            'total_amount',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'id',
            'seller_order',
            'product',
            'product_name',
            'sku',
            'quantity',
            'unit_price',
            'discount_amount',
            'total_price',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'order',
            'payment_method',
            'amount',
            'transaction_id',
            'status',
            'paid_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'transaction_id',
            'paid_at',
            'created_at',
            'updated_at',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'user',
            'order_item',
            'rating',
            'review_text',
            'is_verified_purchase',
            'is_approved',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'is_verified_purchase',
            'is_approved',
            'created_at',
            'updated_at',
        ]


class OrderStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = [
            'id',
            'order',
            'status',
            'changed_by',
            'remarks',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
        ]