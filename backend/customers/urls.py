

from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    CartViewSet,
    CartItemViewSet,
    WishlistViewSet,
    WishlistItemViewSet,
)


router = DefaultRouter()

router.register(
    'addresses',
    AddressViewSet,
    basename='address'
)

router.register(
    'carts',
    CartViewSet,
    basename='cart'
)

router.register(
    'cart-items',
    CartItemViewSet,
    basename='cart-item'
)

router.register(
    'wishlists',
    WishlistViewSet,
    basename='wishlist'
)

router.register(
    'wishlist-items',
    WishlistItemViewSet,
    basename='wishlist-item'
)


urlpatterns = router.urls