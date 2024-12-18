from django.db import models
from store.models import Store

# Create your models here.
    
class Katalog(models.Model):
    CATEGORY_CHOICES = [
        ('hp', 'HP'),
        ('laptop', 'Laptop'),
        ('earphone', 'Earphone')
    ]
        
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    image_link = models.URLField()
    spec = models.CharField(max_length=512)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.brand}"