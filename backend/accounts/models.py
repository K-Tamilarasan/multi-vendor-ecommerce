# Create your models here.

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):

    objects = UserManager()

    user_id = models.BigAutoField(primary_key=True)

    ROLE_CHOICES = [
        ('CUSTOMER', 'Customer'),
        ('SELLER', 'Seller'),
        ('ADMIN', 'Admin'),
    ]

    username = None

    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def __str__(self):
        return self.email
    

    @property
    def is_admin(self):
        return self.role == 'ADMIN' or self.is_superuser
    
    @property
    def is_vendor(self):
        return self.role == 'SELLER'
    
    @property
    def is_customer(self):
        return self.role == 'CUSTOMER'



class SellerProfile(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('SUSPENDED', 'Suspended'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seller_profile'
    )

    store_name = models.CharField(max_length=150, unique=True)
    store_description = models.TextField(null=True, blank=True)
    business_email = models.EmailField(null=True, blank=True)
    business_phone = models.CharField(max_length=15, null=True, blank=True)
    store_logo = models.ImageField(upload_to='vendors/logos/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'seller_profiles'
        ordering = ['-created_at']

    def __str__(self):
        return self.store_name