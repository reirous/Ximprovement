from django.shortcuts import render
from rest_framework import viewsets, generics
from frigobar.models.order import Order
from frigobar.serializers.orderSerializer import OrderSerializer
from django_filters import rest_framework as filters

class OrderFilters(filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'user':['exact',],
            'date': ['lte','gte']}

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_class = OrderFilters