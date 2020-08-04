from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.item import Item
from frigobar.serializers.itemSerializer import ItemSerializer, ItemProductSerializer, ItemConsumedSerializer, ItemConsumedUserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @action(
    methods=["get"],
    detail=False,
    url_path="dopedido/(?P<order_id>[^/.]+)",
    )
    def get_itemsOrder(self, request, order_id, pk=None):
        items = self.get_queryset().filter(order_id=order_id)
        serializer = ItemProductSerializer(items, many=True)
        return Response(data=serializer.data)

    #Falta finalizar
    @action(
        methods=["get"],
        detail=False,
        url_path="consumed",
    )
    def get_consumed(self):
        items = self.get_queryset().annotate(total_cash_in=Sum('price'),
                                             total_accredit=Sum('price'),
                                             total_quantity=Sum('quantity'))
        serializer = ItemConsumedUserSerializer(items, many=True)
        return Response(data=serializer.data)

    # Falta finalizar
    @action(
        methods=["get"],
        detail=False,
        url_path="doUsuario/(?P<user_id>[^/.]+)",
    )
    def get_fromUser(self, user_id, pk=None):
        items = self.get_queryset().filter(user_id=user_id)
        serializer = ItemConsumedSerializer(items, many=True)
