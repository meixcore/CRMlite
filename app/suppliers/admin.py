from django.contrib import admin

from .models import Supplier, Supply, SupplyProduct


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company',
        'title',
        'inn',
    ]

    search_fields = [
        'company',
        'title',
        'inn',
    ]

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'supplier',
        'delivery_date',
    ]
    search_fields = [
        'id',
        'supplier',
        'delivery_date',
    ]

@admin.register(SupplyProduct)
class SupplyProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'supply',
        'product',
        'quantity',
    ]