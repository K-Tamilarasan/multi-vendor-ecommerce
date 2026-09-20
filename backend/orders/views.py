from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from .models import (
    Order,
    SellerOrder,
    OrderItem,
    Payment,
    Review,
    OrderStatusHistory,
)

from .serializers import (
    OrderSerializer,
    SellerOrderSerializer,
    OrderItemSerializer,
    PaymentSerializer,
    ReviewSerializer,
    OrderStatusHistorySerializer,
)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SellerOrderViewSet(ModelViewSet):
    queryset = SellerOrder.objects.all()
    serializer_class = SellerOrderSerializer


class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class OrderStatusHistoryViewSet(ModelViewSet):
    queryset = OrderStatusHistory.objects.all()
    serializer_class = OrderStatusHistorySerializer