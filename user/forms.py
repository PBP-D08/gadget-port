# user/forms.py
from django import forms
from authentication.models import User  

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User  # Menggunakan model Profile
        fields = ['username', 'full_name', 'email', 'alamat', 'bio']  # Tambahkan bio di sini
