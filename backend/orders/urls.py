from rest_framework.routers import DefaultRouter

from .views import (
    OrderViewSet,
    SellerOrderViewSet,
    OrderItemViewSet,
    PaymentViewSet,
    ReviewViewSet,
    OrderStatusHistoryViewSet,
)


router = DefaultRouter()

router.register(
    'orders',
    OrderViewSet,
    basename='order'
)

router.register(
    'seller-orders',
    SellerOrderViewSet,
    basename='seller-order'
)

router.register(
    'order-items',
    OrderItemViewSet,
    basename='order-item'
)

router.register(
    'payments',
    PaymentViewSet,
    basename='payment'
)

router.register(
    'reviews',
    ReviewViewSet,
    basename='review'
)

router.register(
    'order-status-history',
    OrderStatusHistoryViewSet,
    basename='order-status-history'
)


urlpatterns = router.urls