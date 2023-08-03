# from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from products.serializers import ProductSerializer
from products.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # renderer_classes = [JSONRenderer]