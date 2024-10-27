from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('buyer', 'Buyer'),
    ]
    role = models.CharField(max_length=5, choices=ROLES, default='buyer')
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    alamat = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def is_admin(self):
        return self.role == 'Admin'

    def is_buyer(self):
        return self.role == 'Buyer'

    def __str__(self):
        return self.username