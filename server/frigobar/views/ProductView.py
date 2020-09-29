from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.product import Product
from frigobar.models.order import Order
from frigobar.serializers.productSerializer import ProductSerializer, ProductConsumedSerializer
from django.db.models import Sum, F, ExpressionWrapper, DecimalField, Case, When
from django_filters import rest_framework as filters

class ProductFilters(filters.FilterSet):

    class Meta:
        model = Product
        fields = {
            'itemsProduct__order__date': ['range']
        }

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('description')
    serializer_class = ProductSerializer
    filterset_class = ProductFilters

    @action(
    methods=["get"],
    detail=False,
    url_path="actives",
    )
    def get_actives(self, request):
        products = self.get_queryset().filter(status=True)
        serializer = self.serializer_class(products, many=True)

        return Response(data=serializer.data)

    @action(
        methods=["get"],
        detail=False,
        url_path="consumed"
    )
    def get_consumed(self, request):
        products = self.filter_queryset(self.get_queryset()).annotate(
                    total_quantity=Sum('itemsProduct__quantity'),
                    total_cash_in=Sum
                                 (
                                    Case
                                    (
                                        When(itemsProduct__order__orderType=Order.status.SALE,
                                             then=ExpressionWrapper
                                                (
                                                    F('itemsProduct__price') * F('itemsProduct__quantity'),
                                                    output_field=DecimalField()
                                                )
                                             ),
                                        default=0,
                                        output_field=DecimalField()
                                    )
                                ),
                    total_accredit=Sum
                                 (
                                    Case
                                    (
                                        When(itemsProduct__order__orderType=Order.status.BONUS,
                                             then=ExpressionWrapper
                                                (
                                                    F('itemsProduct__price') * F('itemsProduct__quantity'),
                                                    output_field=DecimalField()
                                                )
                                             ),
                                        default=0,
                                        output_field=DecimalField()
                                    )
                                 )
                )
        serializer = ProductConsumedSerializer(products, many=True)
        return Response(data=serializer.data)