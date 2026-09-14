from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="user@test.com",
            password="test12345",
            username="us1",
        )

        self.assertEqual(user.email, "user@test.com")
        self.assertTrue(user.check_password("test12345"))
        self.assertFalse(user.is_company_owner)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="admin@test.com",
            password="test12345",
            username="admin1",
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)