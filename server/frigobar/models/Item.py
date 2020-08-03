from django.db import models
from .order import Order
from .product import Product

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField("Quantity sale")
    price = models.DecimalField("Sale price", max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ('order_id','product_id')