from django.db import models


class Company(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"