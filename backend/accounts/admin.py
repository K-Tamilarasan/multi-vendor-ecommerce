
# Register your models here.

from django.contrib import admin
from .models import User, SellerProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'phone',
        'role',
        'is_active',
        'is_staff',
        'created_at',
    )

    list_filter = (
        'role',
        'is_active',
        'is_staff',
    )

    search_fields = (
        'email',
        'first_name',
        'last_name',
        'phone',
    )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'store_name',
        'user',
        'status',
        'business_email',
        'created_at',
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'store_name',
        'business_email',
        'user__email',
    )