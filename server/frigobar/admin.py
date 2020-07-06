from django.contrib import admin
from .models.Product import Product
from .models.User import User

from django.contrib.auth.models import Group

from .models.User import User

admin.site.register(User)

admin.site.register(Product)
admin.site.unregister(Group)