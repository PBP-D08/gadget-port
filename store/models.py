from authentication.models import User
from django.db import models
import uuid

# Create your models here.
class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)
    logo = models.ImageField(upload_to='store_logo/', blank=True, null=True)
    jam_buka = models.TimeField(default="08:00")  
    jam_tutup = models.TimeField(default="22:00")
    
    def __str__(self):
        return self.nama