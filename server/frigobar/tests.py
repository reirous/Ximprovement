from django.test import TestCase
from django.urls import reverse, resolve
from datetime import date

from frigobar.views.productView import ProductViewSet
from frigobar.models.product import Product


class ProductsUrlsTestCase(TestCase):

    def test_product_create(self):
        product = Product.objects.create(
            description="Coca Cola", status=True, price=5, priceDate=date.today(), barCode="1234567890123"
        )

        product_result = Product.objects.last()

        self.assertEqual(product_result.description, "Coca Cola")