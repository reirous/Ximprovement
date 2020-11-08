from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from frigobar.models.photo import Photo
from frigobar.serializers.photoSerializer import PhotoSerializer
from django_filters import rest_framework as filters
from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
import coreapi
import coreschema

class PhotoFilters(filters.FilterSet):

    class Meta:
        model = Photo
        fields = {
            'photoType':['exact',],
        }

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    filterset_class = PhotoFilters

    @action(
        methods=['get'],
        detail=True,
        url_path='download',
        schema=ManualSchema(
            fields=[
                coreapi.Field(
                    "id",
                    required=True,
                    location="path",
                    schema=coreschema.Integer(),
                    description="File id",
                )
            ], description="Download a file"
        ),
    )
    def download_file(self, request, pk):
        """Download a loan application document"""
        #file = self.get_object()
        file = open("e:\\test.jpg", 'rb')
        response = FileResponse(file, content_type='img/jpg')
        #response['Content-Length'] = len(file)
        response['Content-Disposition'] = 'attachment; filename="test.jpg​​​​​"'

        return response
