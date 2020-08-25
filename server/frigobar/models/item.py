from django.db import models
from .order import Order
from .product import Product

class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='itemsProduct')
    quantity = models.IntegerField("Quantity sale")
    price = models.DecimalField("Sale price", max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ('order_id','product_id')

    @property
    def quantity_cash_in(self):
        if self.order.orderType == self.order.status.SALE:
            return self.quantity
        else:
            return 0
    @property
    def quantity_accredit(self):
        if self.order.orderType != self.order.status.SALE:
            return self.quantity
        else:
            return 0

    @property
    def total_cash_in(self):
        if self.order.orderType == self.order.status.SALE:
            return self.quantity * self.price
        else:
            return 0

    @property
    def total_accredit(self):
        if self.order.orderType != self.order.status.SALE:
            return self.quantity * self.price
        else:
            return 0