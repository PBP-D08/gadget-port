# user/forms.py
from django import forms
from .models import Profile  # Adjust this import

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Use Profile if SubProfile doesn't exist
        fields = ['username', 'full_name', 'email', 'alamat']

class SubProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Use Profile again if SubProfile is meant to refer to Profile
        fields = ['full_name', 'email', 'alamat']
