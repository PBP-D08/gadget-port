from django.forms import ModelForm
from products.models import Katalog

class ProductEntryForm(ModelForm):
    class Meta:
        model = Katalog
        fields = ["category", "name", "brand", "price", "image_link", "spec"]