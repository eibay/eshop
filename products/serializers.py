from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "sku", "price", "description", "quantity", "status"]
        read_only_fields = ('id',) 