from datetime import date

from django.test import TestCase

from users.models import User
from company.models import Company
from storage.models import Storage, Product
from .models import Sale, ProductSale


class SaleModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="owner@test.com",
            password="test12345",
            username="owner",
        )

        self.company = Company.objects.create(
            title="Test Company",
            inn="test_inn",
        )

        self.storage = Storage.objects.create(
            address="Склад 1",
            company=self.company,
        )

        self.product = Product.objects.create(
            title="Ноутбук",
            purchase_price=1000,
            sale_price=500,
            quantity=2,
            storage=self.storage,
        )

    def test_create_product_sale(self):
        sale = Sale.objects.create(
            buyer_name="Иван Иванов",
            company=self.company,
        )

        product_sale = ProductSale.objects.create(
            sale=sale,
            product=self.product,
            quantity=2,
        )

        self.assertEqual(product_sale.sale, sale)
        self.assertEqual(product_sale.product, self.product)
        self.assertEqual(product_sale.quantity, 2)