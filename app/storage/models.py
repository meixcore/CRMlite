from django.db import models

#Storage, Product

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

class Product(models.Model):
    title = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    storage = models.ForeignKey(
        Storage,
        on_delete=models.CASCADE,
        related_name='products',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"