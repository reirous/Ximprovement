from rest_framework import serializers
from frigobar.models.product import Product 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 0
        fields = "__all__"