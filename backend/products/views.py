from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

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


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer