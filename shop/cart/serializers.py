from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'product', 'quantity', 'total_price', 'total_quantity')

    def get_total_price(self, obj):
        return obj.quantity * obj.product.price

    def get_total_quantity(self, obj):
        return obj.quantity