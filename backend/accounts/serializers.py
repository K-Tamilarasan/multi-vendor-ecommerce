from rest_framework import serializers
from .models import User, SellerProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'role',
            'is_active',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'user_id',
            'created_at',
            'updated_at',
        ]


class SellerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerProfile
        fields = [
            'id',
            'user',
            'store_name',
            'store_description',
            'business_email',
            'business_phone',
            'store_logo',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]