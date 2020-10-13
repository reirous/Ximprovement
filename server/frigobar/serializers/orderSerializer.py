from rest_framework import serializers
from frigobar.models.order import Order
from frigobar.models.item import Item
from django.db.transaction import atomic

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

class ItemSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 0
        exclude = ("order",)


class OrderItemSerializer(serializers.ModelSerializer):

    items = ItemSerializer2(many=True)

    class Meta:
        model = Order
        depth = 0
        fields = ["user", "orderType", "justification", "date", "items"]

    @atomic
    def create(self, validated_data):
        items = validated_data.pop('items')
        instance = Order.objects.create(**validated_data)
        for item in items:
            instance.items.add(Item.objects.create(**item, order=instance))
            #teste = Item.objects.create(**item, order=instance)

        return instance