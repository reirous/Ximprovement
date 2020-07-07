from django.shortcuts import render
from rest_framework import viewsets
from frigobar.models.Order import Order
from frigobar.serializers.OrderSerializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer