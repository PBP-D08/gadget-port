from django.contrib import admin
from .models import *

# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    list_display=('user', 'product', 'review_text', 'rating', 'timestamp')
admin.site.register(Review, ProductReviewAdmin)