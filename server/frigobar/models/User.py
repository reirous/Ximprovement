from django.db import models

class User(models.Model):
    name = models.CharField("User namer", max_length=50)
    description = models.CharField("User description", max_length=100)
    lastLogin = models.DateTimeField("User last login date")
    admin = models.BooleanField("User is admin", default=False)