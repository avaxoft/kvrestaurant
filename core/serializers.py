from rest_framework import serializers
from .models import Item, Deal, DealItem, Order


class ItemSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Item
        fields = "__all__"
class DealSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Deal
        fields = "__all__"

class DealItemsSerializer(serializers.ModelSerializer):
    item = serializers.CharField(source='item.name')
    class Meta:
        model = DealItem
        fields = "__all__"

class DealsSerializer(serializers.ModelSerializer):
    dealitems = DealItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Deal
        fields = "__all__"

class ItemsDealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']
    
class DealItemSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = DealItem
        fields = "__all__"
class OrderSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"