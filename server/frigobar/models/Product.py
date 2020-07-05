from django.db import models

class Product(models.Model):
    description = models.CharField("Product's description", max_length=100)
    status = models.BooleanField("Product's active", default=True)
    price = models.DecimalField("Product's price", max_digits=15, decimal_places=2) 
    priceDate = models.DateTimeField("Price date")