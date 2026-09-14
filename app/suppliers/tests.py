from django.test import TestCase

from users.models import User
from company.models import Company
from .models import Supplier, Supply


class SupplierModelTest(TestCase):

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

    def test_create_supplier(self):
        supplier = Supplier.objects.create(
            title="Поставщик 1",
            inn="test_inn",
            company=self.company,
        )

        self.assertEqual(supplier.title, "Поставщик 1")
        self.assertEqual(supplier.company, self.company)
        self.assertEqual(supplier.inn, "test_inn")

class SupplyModelTest(TestCase):

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

        self.supplier = Supplier.objects.create(
            title="Поставщик 1",
            inn="test_inn",
            company=self.company,
        )

    def test_create_supply(self):
        supply = Supply.objects.create(
            supplier=self.supplier,
        )

        self.assertEqual(supply.supplier, self.supplier)