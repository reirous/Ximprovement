from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.photo import Photo
from frigobar.serializers.photoSerializer import PhotoSerializer
from django_filters import rest_framework as filters

class PhotoFilters(filters.FilterSet):

    class Meta:
        model = Photo
        fields = {
            'photoType':['exact',],
        }

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all().order_by('description')
    serializer_class = PhotoSerializer
    filterset_class = PhotoFilters