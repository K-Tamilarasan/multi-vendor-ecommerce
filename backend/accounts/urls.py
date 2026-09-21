from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()

router.register(
    'users',
    UserViewSet,
    basename='user'
)

# router.register(
#     'seller-profiles',
#     SellerProfileViewSet,
#     basename='seller-profile'
# )

urlpatterns = router.urls