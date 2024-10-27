# user/forms.py
from django import forms
from authentication.models import Profile  # Pastikan mengimpor dari model Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Menggunakan model Profile
        fields = ['username', 'full_name', 'email', 'alamat', 'bio']  # Tambahkan bio di sini
