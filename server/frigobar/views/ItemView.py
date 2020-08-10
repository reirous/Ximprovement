from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.item import Item
from frigobar.serializers.itemSerializer import ItemSerializer, ItemProductSerializer, ItemConsumedUserSerializer
from django_filters import rest_framework as filters

class ItemFilters(filters.FilterSet):

    class Meta:
        model = Item
        fields = {
            'order__date': ['lte','gte']
        }

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_class = ItemFilters

    @action(
    methods=["get"],
    detail=False,
    url_path="dopedido/(?P<order_id>[^/.]+)",
    )
    def get_itemsOrder(self, request, order_id):
        items = self.get_queryset().filter(order_id=order_id)
        serializer = ItemProductSerializer(items, many=True)
        return Response(data=serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path="doUsuario/(?P<user_id>[^/.]+)"
    )
    def get_fromUser(self, request, user_id):
        items = self.filter_queryset(self.get_queryset().filter(order__user_id=user_id))
        serializer = ItemConsumedUserSerializer(items, many=True)
        return Response(data=serializer.data)
