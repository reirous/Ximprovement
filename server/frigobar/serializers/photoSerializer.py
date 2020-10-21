from rest_framework import serializers
from frigobar.models.photo import Photo

class PhotoSerializer(serializers.ModelSerializer):
    photo = serializers.FileField()

    class Meta:
        model = Photo
        depth = 0
        fields = ["id", "product", "photoType", "photo"]