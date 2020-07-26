from django.shortcuts import render
from rest_framework import viewsets
from frigobar.models.item import Item
from frigobar.serializers.itemSerializer import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer