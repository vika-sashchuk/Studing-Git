from django.test import TestCase
from shop.models import Shop


class ShopTestCase(TestCase):
    def testPost(self):
        shop = Shop(name="Test Shop", address="Test Address", shop_type="Store")
        self.assertEqual(shop.name, "Test Shop")
        self.assertEqual(shop.address, "Test Address")
        self.assertEqual(shop.shop_type, "Store")