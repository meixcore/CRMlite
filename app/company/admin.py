from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "inn",
    ]

    search_fields = [
        "title",
        "inn",
    ]