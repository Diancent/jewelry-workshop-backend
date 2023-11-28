from rest_framework import serializers
from base.models import Item, Customer, Product, Artisan, Order, OrderItem, Material

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ArtisanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artisan
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class RequestSerializer(serializers.Serializer):
    unique_id = serializers.CharField(max_length=50, allow_null=False, allow_blank=True)
    sentence_list = serializers.ListField(
        child=serializers.CharField(allow_blank=False, trim_whitespace=True)
    )
