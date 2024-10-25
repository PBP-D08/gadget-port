from django.db import models

# Create your models here.

class Katalog(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.IntegerField()
    # image_link = models.ImageField()
    spec = models.CharField(max_length=255)