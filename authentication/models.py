from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=5)
    username = models.CharField(max_length=30)
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    alamat = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def is_admin(self):
        return self.role == 'Admin'

    def is_buyer(self):
        return self.role == 'Buyer'

    def __str__(self):
        return self.user.username