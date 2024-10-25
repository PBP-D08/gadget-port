from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['nama', 'alamat', 'jam_buka', 'jam_tutup', 'nomor_telepon', 'logo']