import uuid
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
    
class Katalog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
    image_link = models.ImageField()
    spec = models.CharField(max_length=512)