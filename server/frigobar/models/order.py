from django.db import models
from .user import User

class OrderType:
    SALE = 1
    BONUS = 2
    DELETED = 3

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderType = models.IntegerField()
    justification = models.CharField("Order justification", max_length=150, default=None, blank=True, null=True)
    date = models.DateTimeField("Order date")
    
    status = OrderType()