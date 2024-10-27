# Register your models here.
from django.contrib import admin
from .models import UserProfile

admin.site.register(UserProfile)

class UserProfile(admin.ModelAdmin):
    fields = ['username', 'fullname', 'email', 'alamat']
