from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.order import Order
from frigobar.serializers.orderSerializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderGetUser(ListAPIView):    
    serializer_class = OrderSerializer

    def get_queryset (self):
        user = self.kwargs.get('user')
        return Order.objects.filter(user=user)


class OrderGetDate(ListAPIView):
    serializer_class = OrderSerializer
    
    def get_queryset (self):
        user = self.kwargs.get('user', None)
        start = self.kwargs.get('start', None)
        end = self.kwargs.get('end', None)
        return Order.objects.filter(user=user, date__range=[start, end])