from django.db import models
from .product import Product


class PhotoType:
    WAITING = 0
    APPROVED = 1
    DISAPPROVED = 2


class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    photoType = models.IntegerField()
    directory = models.CharField("Photo directory", max_length=150, default=None, blank=True, null=True)

    status = PhotoType()