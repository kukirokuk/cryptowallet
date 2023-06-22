from django.urls import path, include
from rest_framework.routers import DefaultRouter
from crypto_addresses.views import AddressViewSet

router = DefaultRouter()
router.register(r"addresses", AddressViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
