from rest_framework import serializers
from frigobar.models.order import Order
from frigobar.models.item import Item
from frigobar.serializers.itemSerializer import ItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        depth = 0
        fields = '__all__'


class OrderTotalSerializer(serializers.ModelSerializer):
    total_cash_in = serializers.DecimalField(15, 2, read_only=True)
    total_accredit = serializers.DecimalField(15, 2, read_only=True)
    total = serializers.DecimalField(15, 2, read_only=True)
    name = serializers.CharField(source='order.user.first_name', read_only=True)

    class Meta:
        model = Order
        depth = 0
        fields = ["id", "user", "orderType", "date", "justification", "name", "total_accredit", "total_cash_in", "total"]

class OrderPeriodSerializer(serializers.ModelSerializer):
    month = serializers.CharField()
    year = serializers.CharField()

    class Meta:
        model = Order
        depth = 0
        fields = ["month", "year"]

class OrderItemSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        depth = 0
        fields = ["user", "orderType", "justification", "date", "items"]

    def create(self, validated_data):
        items = validated_data.pop('items')
        instance = Order.objects.create(**validated_data)
        for item in items:
            teste = Item.objects.create(item)

        return instance