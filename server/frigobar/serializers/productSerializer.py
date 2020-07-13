from rest_framework import serializers
from frigobar.models.product import Product 

class ProductSerializer(serializers.ModelSerializer):  # TODO Se atentar às convenções para organização do código (nesse caso duas linhas em branco antes da classe)
    class Meta:
        model = Product
        depth = 0
        fields = "__all__"