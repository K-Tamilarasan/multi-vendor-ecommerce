
# Register your models here.

from django.contrib import admin
from django.contrib.auth.hashers import is_password_usable, identify_hasher
from .models import User, SellerProfile


# admin.site.register(User)
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

    def save_model(self, request, obj, form, change):
        # Admin-la password enter panniruntha, athu already hashed-aa illayana hash pannum
        if obj.password:
            try:
                identify_hasher(obj.password)
            except ValueError:
                # Value plain text-aa iruntha ValueError throw pannum, so inga hash aagidum
                obj.set_password(obj.password)
        super().save_model(request, obj, form, change)




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