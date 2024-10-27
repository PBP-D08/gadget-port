from django.db import models
from authentication.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

    # Field lain yang relevan untuk UserProfile
    parent_profile = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='sub_profile',
        help_text="Only buyers can have additional profiles."
    )

    def can_add_sub_profile(self):
        return self.profile.role == "Buyer"

    def str(self):
        return f"{self.profile.full_name}'s profile"