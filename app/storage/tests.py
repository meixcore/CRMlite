from django.test import TestCase

from users.models import User
from company.models import Company
from .models import Storage, Product


class StorageModelTest(TestCase):

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

    def test_create_storage(self):
        storage = Storage.objects.create(
            address="Санкт-Петербург",
            company=self.company,
        )

        self.assertEqual(storage.address, "Санкт-Петербург")
        self.assertEqual(storage.company, self.company)

class ProductModelTest(TestCase):

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

    def test_create_product(self):
        product = Product.objects.create(
            title="Ноутбук",
            storage=self.storage,
            purchase_price=100,
            sale_price=50,
            quantity=1,
        )

        self.assertEqual(product.title, "Ноутбук")
        self.assertEqual(product.storage, self.storage)
        self.assertEqual(product.purchase_price, 100)
        self.assertEqual(product.sale_price, 50)
        self.assertEqual(product.quantity, 1)