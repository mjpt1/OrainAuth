from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import OrainAuth


@admin.register(OrainAuth)
class OrainAuthAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('OrainAuth', {'fields': ('cash',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('OrainAuth', {'fields': ('cash',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'cash', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
