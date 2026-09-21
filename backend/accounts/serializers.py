from rest_framework import serializers
from .models import User, SellerProfile


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'password',
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

        def create(self, validated_data):
            password = validated_data.pop('password')

            # user = User.objects.create_user(password=password,**validated_data)

            # return user
            user = User(**validated_data)

            user.set_password(password)

            user.save()

            return user


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