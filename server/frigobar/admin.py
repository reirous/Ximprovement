from django.contrib import admin
from .models.product import Product
from .models.user import User

from django.contrib.auth.models import Group

admin.site.register(User)

admin.site.register(Product)
admin.site.unregister(Group)