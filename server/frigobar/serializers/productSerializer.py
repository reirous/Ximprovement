from rest_framework import serializers
from frigobar.models.product import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 0
        fields = "__all__"

class ProductConsumedSerializer(serializers.ModelSerializer):
    total_cash_in = serializers.DecimalField(15,2,read_only=True)
    total_accredit = serializers.DecimalField(15,2,read_only=True)
    total_quantity = serializers.IntegerField()

    class Meta:
        model = Product
        depth = 0
        fields = ["id", "description", "total_quantity", "total_cash_in", "total_accredit"]

