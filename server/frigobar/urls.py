"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url
from frigobar.views.productView import ProductViewSet
from frigobar.views.orderView import OrderViewSet
from frigobar.views.itemView import ItemViewSet
from frigobar.views.userView import RegisterAPI
from frigobar.views.loginView import LoginAPI
from rest_framework import routers
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'produtos', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),    
]
