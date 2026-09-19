
# Register your models here.

from django.contrib import admin
from .models import (
    Order,
    SellerOrder,
    OrderItem,
    Payment,
    Review,
    OrderStatusHistory,
)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'user',
        'address',
        'total_amount',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'order_number',
        'user__email',
    )


@admin.register(SellerOrder)
class SellerOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'seller',
        'subtotal',
        'shipping_fee',
        'total_amount',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'order__order_number',
        'seller__store_name',
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'seller_order',
        'product',
        'product_name',
        'quantity',
        'unit_price',
        'total_price',
        'created_at',
    )

    search_fields = (
        'product_name',
        'sku',
        'seller_order__order__order_number',
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'payment_method',
        'amount',
        'transaction_id',
        'status',
        'paid_at',
        'created_at',
    )

    list_filter = (
        'payment_method',
        'status',
    )

    search_fields = (
        'order__order_number',
        'transaction_id',
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'is_verified_purchase',
        'is_approved',
        'created_at',
    )

    list_filter = (
        'rating',
        'is_verified_purchase',
        'is_approved',
    )

    search_fields = (
        'product__name',
        'user__email',
        'review_text',
    )


@admin.register(OrderStatusHistory)
class OrderStatusHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'order',
        'status',
        'changed_by',
        'remarks',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'order__order_number',
        'changed_by__email',
        'remarks',
    )