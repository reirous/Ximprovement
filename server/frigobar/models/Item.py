from django.db import models
from .Order import Order
from .Product import Product

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity sale")
    price = models.DecimalField("Sale price", max_digits=15, decimal_places=2)