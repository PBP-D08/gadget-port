# wishlist/models.py

from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Katalog
# from authentication.models import Profile
from django.db.models import UniqueConstraint
from authentication.models import User
from products.models import Katalog

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Katalog, on_delete=models.CASCADE, related_name='wishlist_items', null=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'product'], name='unique_user_product_wishlist')
        ]
        verbose_name = 'Wishlist'
        verbose_name_plural = 'Wishlists'
        ordering = ['-added_on']

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'