from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=20)
    jam_buka = models.TimeField()
    jam_tutup = models.TimeField()
    logo = models.URLField(max_length=500)  # Changed to URLField
    
    def __str__(self):
        return self.nama