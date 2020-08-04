from rest_framework import serializers
from frigobar.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 0
        fields = "__all__"


class ItemProductSerializer(serializers.ModelSerializer):
    description = serializers.CharField(source='product.description', read_only=True)
    usuario = serializers.CharField(source='order.user.username', read_only=True)

    class Meta:
        model = Item
        depth = 0
        fields = ["id", "order_id", "quantity", "price", "description", "usuario"]

#Falta finalizar
class ItemConsumedSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id', read_only=True)
    total_cash_in = serializers.DecimalField(15,2)
    total_accredit = serializers.DecimalField(15,2)
    total_quantity = serializers.IntegerField()

    class Meta:
        model = Item
        depth = 0
        fields = ["product_id", "description", "total_quantity", "total_cash_in", "total_accredit"]

#Falta finalizar
class ItemConsumedUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='order.user.id', read_only=True)
    date = serializers.DateField(source='order.date', read_only=True)
    justification = serializers.CharField(source='order.justification', read_only=True)
    orderType =serializers.CharField(source='order.orderType', read_only=True)
    quantity_cash_in = serializers.DecimalField(15,2)
    quantity_accredit = serializers.DecimalField(15,2)
    class Meta:
        model = Item
        depth = 0
        fields = ["user_id",
                  "date",
                  "justification",
                  "orderType",
                  "description",
                  "price",
                  "quantity",
                  "quantity_cash_in",
                  "quantity_accredit"]