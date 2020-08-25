from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.order import Order
from frigobar.serializers.orderSerializer import OrderSerializer, OrderTotalSerializer
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Case, When
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

    @action(
        methods=["get"],
        detail=True,
        url_path="total",
    )
    def get_total(self, request, pk):
        order = self.filter_queryset(self.get_queryset().filter(id=pk)).annotate(            
            total_cash_in=Sum(
                Case(
                    When(orderType=Order.status.SALE,
                        then=ExpressionWrapper
                        (
                            F('items__price') * F('items__quantity'),
                            output_field=DecimalField()
                        ) 
                    ),
                    default = 0,
                    output_field=DecimalField()
                )
            ),
            total_accredit=Sum(
                Case(
                    When(orderType=Order.status.BONUS,
                        then=ExpressionWrapper
                        (
                            F('items__price') * F('items__quantity'),
                            output_field=DecimalField()
                        ) 
                    ),
                    default = 0,
                    output_field=DecimalField()
                )
            ),
        )
        serializer = OrderTotalSerializer(order, many=True)
        return Response(data=serializer.data)