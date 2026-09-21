from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsSeller

from .models import (
    Category,
    Product,
    ProductImage,
    Inventory,
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductImageSerializer,
    InventorySerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsSeller]


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer