# wishlist/models.py

from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Katalog
# from authentication.models import Profile
from django.contrib.auth.models import User
from products.models import Katalog

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Wishlist")

class WishlistItem(models.Model):
    katalog = models.ForeignKey(Katalog, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    is_purchased = models.BooleanField(default=False)
