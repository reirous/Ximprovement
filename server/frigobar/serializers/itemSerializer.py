from rest_framework import serializers
from frigobar.models.item import Item 

class ItemSerializer(serializers.ModelSerializer):  # TODO Se atentar às convenções para organização do código (nesse caso duas linhas em branco antes da classe)
    class Meta:
        model = Item
        depth = 0
        fields = "__all__"