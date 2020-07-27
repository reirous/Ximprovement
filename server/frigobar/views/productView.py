from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins  import UpdateModelMixin
from frigobar.models.product import Product
from frigobar.serializers.productSerializer import ProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('description')
    serializer_class = ProductSerializer

class ProductGetActiveView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(status=True)

class ProductPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Allows to edit chosen fields
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)