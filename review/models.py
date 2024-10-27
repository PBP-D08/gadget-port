from django.db import models
from authentication.models import User
from products.models import *
from datetime import datetime
from django.db.models import Avg

# Create your models here .
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=1, choices=((i,i) for i in range(1, 6)))
    product = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def update_rating(self):
        avg_rating = Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        if avg_rating is not None:
            self.rating = avg_rating
            self.save()
        else:
            self.rating = 0.0
            self.save()

    def __str__(self):
        return f"{self.user.username} - {self.product.name}: {self.rating}"