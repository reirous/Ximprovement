from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.product import Product
from frigobar.serializers.productSerializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('description')
    serializer_class = ProductSerializer

    @action(
    methods=["get"],
    detail=False,
    url_path="ativos",
    )
    def get_actives(self, request):
        products = self.get_queryset().filter(status=True)
        serializer = self.serializer_class(products, many=True)
        return Response(data=serializer.data)