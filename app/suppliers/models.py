from django.db import models

#Supplier, Supply, SupplyProduct

class Supplier(models.Model):
    company = models.ForeignKey(
        'company.Company',
        on_delete=models.CASCADE,
        related_name='supplier',
    )
    inn = models.CharField(max_length=12, unique=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

class Supply(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='supplies',
    )
    delivery_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        "storage.Product",
        through="SupplyProduct",
        related_name="supplies",
    )

    def __str__(self):
        return f"Поставка {self.id} от {self.delivery_date:%d.%m.%Y}, поставщик - {self.supplier_id}"

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"

class SupplyProduct(models.Model):
    supply = models.ForeignKey(
        Supply,
        on_delete=models.CASCADE,
        related_name='supply_products',
    )
    product = models.ForeignKey(
        'storage.Product',
        on_delete=models.CASCADE,
        related_name='supply_products',
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return (
            f'Поставка: {self.supply}'
            f'Товар: {self.product}'
            f'Количество: {self.quantity}'
        )

    class Meta:
        verbose_name = "Товар в поставке"
        verbose_name_plural = "Товар в поставках"