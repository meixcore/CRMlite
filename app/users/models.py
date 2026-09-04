from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    is_company_owner = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'