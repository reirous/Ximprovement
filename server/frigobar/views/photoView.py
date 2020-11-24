from rest_framework import viewsets
from rest_framework.response import Response
from frigobar.models.photo import Photo
from frigobar.serializers.photoSerializer import PhotoSerializer
from django_filters import rest_framework as filters
from django.http import FileResponse
from rest_framework.decorators import action
from rest_framework.schemas import ManualSchema
import coreapi
import coreschema
from rest_framework import status
import os
import errno
import base64

class PhotoFilters(filters.FilterSet):

    class Meta:
        model = Photo
        fields = {
            'photoType':['exact',],
            'product':['exact',],
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
        photo = self.get_object()
        filePath = photo.directory + str(photo.id) + ".jpg"
        file = open(filePath, 'rb')
        response = FileResponse(file, content_type='img/jpeg')
        tamanho = os.path.getsize(filePath)
        response['Content-Length'] = tamanho
        response['Content-Disposition'] = 'attachment; filename="' + str(photo.id) + '.jpg"'

        return response

    def destroy(self, request, *args, **kwargs):
        photo = self.get_object()
        filePath = photo.directory + str(photo.id) + ".jpg"
        try:
            os.remove(filePath)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

        self.perform_destroy(photo)
        return Response(status=status.HTTP_200_OK)