from django.db import models
from django.conf import settings  # Import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')

    # Additional fields for UserProfile
    parent_profile = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='sub_profile',
        help_text="Only buyers can have additional profiles."
    )

    def can_add_sub_profile(self):
        return self.user.role == "Buyer"  # Perbaiki di sini

    def __str__(self):
        return f"{self.user.username}'s profile"  # Perbaiki di sini
