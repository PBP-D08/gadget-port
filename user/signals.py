# user/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from authentication.models import Profile
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Buat Profile terlebih dahulu
        profile = Profile.objects.create(user=instance)
        # Sekarang buat UserProfile
        UserProfile.objects.create(profile=profile)
