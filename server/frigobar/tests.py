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

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name('produtos')

        self.assertEqual(resolver.func.cls, ProductViewSet)

    def test_resolves_retrieve_url(self):
        resolver = self.resolve_by_name('produtos', pk=1)

        self.assertEqual(resolver.func.cls, ProductViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = self.resolve_by_name('produtos')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = self.resolve_by_name('produtos', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])

    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)