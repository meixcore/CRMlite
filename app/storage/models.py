from django.db import models


class Storage(models.Model):
    address = models.CharField(max_length=255)
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name='storages',
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"