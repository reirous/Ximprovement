from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from frigobar.models.order import Order
from frigobar.serializers.orderSerializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def put (self, request, *arg, **kwargs):
        return self.partial_update(request, *arg, **kwargs)