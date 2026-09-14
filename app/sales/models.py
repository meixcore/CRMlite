from django.utils import timezone
from django.db import models

# Sale, ProductSale

class Sale(models.Model):
    buyer_name = models.CharField(max_length=100)
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name='sales',
    )
    sale_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Продажа {self.id}: {self.buyer_name} от {self.sale_date}'

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

class ProductSale(models.Model):
    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='product_sales',
    )
    product = models.ForeignKey(
        'storage.Product',
        on_delete=models.CASCADE,
        related_name='product_sales',
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'Продажа {self.id}: товар {self.product_id}, количество {self.quantity}'