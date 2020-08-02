from rest_framework import serializers
from frigobar.models.item import Item 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        depth = 0
        fields = "__all__"