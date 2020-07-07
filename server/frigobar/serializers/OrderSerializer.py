from rest_framework import serializers
from frigobar.models.Order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        depth = 0
        fields = '__all__'