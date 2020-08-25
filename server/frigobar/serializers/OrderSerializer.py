from rest_framework import serializers
from frigobar.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        depth = 0
        fields = '__all__'


class OrderTotalSerializer(serializers.ModelSerializer):
    total_cash_in = serializers.DecimalField(15,2,read_only=True)
    total_accredit = serializers.DecimalField(15,2,read_only=True)

    
    class Meta:
        model = Order
        depth = 0
        fields = ["id","user","date","total_accredit","total_cash_in"]
