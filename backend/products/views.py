from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
#
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

# from accounts.permissions import IsSeller
from accounts.permissions import IsSellerOrAdmin
#
from .models import (Category,Product,ProductImage,Inventory,)
from .models import Product
#
from .serializers import (CategorySerializer,ProductSerializer,ProductImageSerializer,InventorySerializer,)
from .serializers import ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsSeller]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsSellerOrAdmin()]

    def perform_create(self, serializer):
        if self.request.user.role == 'ADMIN':
            serializer.save()
        else:
            serializer.save(
                seller=self.request.user.seller_profile
            )


class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer