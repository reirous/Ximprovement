from rest_framework import serializers
from frigobar.models.photo import Photo
from drf_extra_fields.fields import Base64ImageField
import os
import errno
from django.db.transaction import atomic

class PhotoSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False)

    class Meta:
        model = Photo
        depth = 0
        fields = ["id", "product", "photoType", "photo"]

    @atomic
    def create(self, validated_data):

        filePath = "c:\\frigobar\\" + str(validated_data['product'].id) + "\\"

        instance = Photo.objects.create(
            product=validated_data['product'], photoType=validated_data['photoType'], directory=filePath
        )

        filePath += str(instance.id) + ".jpg"
        if not os.path.exists(os.path.dirname(filePath)):
            try:
                os.makedirs(os.path.dirname(filePath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise

        imgdata = validated_data['photo'].file.read()
        with open(filePath, 'w+b') as file:
            file.write(imgdata)

        return instance