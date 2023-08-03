from django.urls import path, include
from rest_framework import routers

from products.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = [
    path("api/", include(router.urls)),
]