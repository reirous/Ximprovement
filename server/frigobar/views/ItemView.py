from django.shortcuts import render
from rest_framework import viewsets
from frigobar.models.Item import Item
from frigobar.serializers.ItemSerializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer