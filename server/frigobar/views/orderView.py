from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.order import Order
from frigobar.serializers.orderSerializer import OrderSerializer, OrderTotalSerializer, OrderPeriodSerializer, OrderItemSerializer
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Case, When
from django_filters import rest_framework as filters
from django.db.models.functions import ExtractMonth, ExtractYear
import datetime

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
            total=Sum(ExpressionWrapper
                        (
                            F('items__price') * F('items__quantity'),
                            output_field=DecimalField()
                        )
            ),
        )
        serializer = OrderTotalSerializer(order, many=True)
        return Response(data=serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path="all",
    )
    def get_all(self, request):
        order = self.filter_queryset(self.get_queryset()).annotate(
            total_cash_in=Sum(
                Case(
                    When(orderType=Order.status.SALE,
                         then=ExpressionWrapper
                             (
                             F('items__price') * F('items__quantity'),
                             output_field=DecimalField()
                         )
                         ),
                    default=0,
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
                    default=0,
                    output_field=DecimalField()
                )
            ),
            total=Sum(ExpressionWrapper
                (
                F('items__price') * F('items__quantity'),
                output_field=DecimalField()
            )
            ),
        )
        serializer = OrderTotalSerializer(order, many=True)
        return Response(data=serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path="period",
    )
    def get_period(self, request):
        periods = self.filter_queryset(self.get_queryset()).annotate(
            month=ExtractMonth('date'), year=ExtractYear('date')
        ).values('month','year').distinct()
        serializer = OrderPeriodSerializer(periods, many=True)

        months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
                 'Novembro', 'Dezembro']
        monthsList = []

        for aux in serializer.data:
            monthsList.append({'value': datetime.date(int(aux['year']), int(aux['month']) - 1, 1), 'label': months[int(aux['month']) - 1] + ' ' + aux['year']})

        return Response(data=monthsList)
