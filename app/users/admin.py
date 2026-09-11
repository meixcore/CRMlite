from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','is_superuser', 'is_active', 'company', 'is_company_owner')
    list_display_links = ('id', 'username', 'email')