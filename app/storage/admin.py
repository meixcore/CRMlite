from django.contrib import admin

from .models import Storage, Product


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "address",
        "company",
    ]

    search_fields = [
        "address",
        "company",
    ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]