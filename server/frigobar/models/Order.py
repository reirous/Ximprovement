from django.db import models
from .User import User

class Order(models.Model):
    SALE = 0
    BONUS = 1
    Status = (
        (SALE, 'Sales Order'),
        (BONUS, 'Bonus Order')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderType = models.IntegerField(choices=Status, default=SALE)
    justification = models.CharField("Order justification", max_length=150, default=None, blank=True, null=True)
    date = models.DateTimeField("Order date")