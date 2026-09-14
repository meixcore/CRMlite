from django.test import TestCase

from users.models import User
from .models import Company


class CompanyModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="owner@test.com",
            password="test12345",
            username="owner",
        )

    def test_create_company(self):
        company = Company.objects.create(
            title="Test Company",
            inn="inn_1",
        )

        self.assertEqual(company.title, "Test Company")
        self.assertEqual(company.inn, "inn_1")