from django.test import TestCase
from django.urls import reverse, resolve
from datetime import date

from frigobar.views.productView import ProductViewSet
from frigobar.views.itemView import ItemViewSet
from frigobar.models.product import Product


class UrlsTestCast(TestCase):
    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)

class ProductsUrlsTestCase(UrlsTestCast):

    def test_product_create(self):
        product = Product.objects.create(
            description="Coca Cola", status=True, price=5, priceDate='2016-01-02 00:00+0000', barCode="1234567890123"
        )

        product_result = Product.objects.last()

        self.assertEqual(product_result.description, "Coca Cola")

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name('product-list')

        self.assertEqual(resolver.func.cls, ProductViewSet)

    def test_resolves_retrieve_url(self):
        resolver = self.resolve_by_name('product-detail', pk=1)

        self.assertEqual(resolver.func.cls, ProductViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = self.resolve_by_name('product-list')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = self.resolve_by_name('product-detail', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])

    def test_resolves_actives_url(self):
        resolver = self.resolve_by_name('product-get-actives')

        self.assertEqual(resolver.func.cls, ProductViewSet)


    def test_resolves_consumed_url(self):
        resolver = self.resolve_by_name('product-get-consumed')

        self.assertEqual(resolver.func.cls, ProductViewSet)


class ItemUrlsTestCase(UrlsTestCast):

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name('item-list')

        self.assertEqual(resolver.func.cls, ItemViewSet)

    def test_resolves_retrieve_url(self):
        resolver = self.resolve_by_name('item-detail', pk=1)

        self.assertEqual(resolver.func.cls, ItemViewSet)

    def test_resolves_url_to_list_action(self):
        resolver = self.resolve_by_name('item-list')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_resolves_url_to_retrieve_action(self):
        resolver = self.resolve_by_name('item-detail', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])

    def test_resolves_itemsOrder_url(self):
        resolver = self.resolve_by_name('item-get-itemsOrder', order_id=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])


    def test_resolves_fromUser_url(self):
        resolver = self.resolve_by_name('item-get-fromUser', user_id=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

