from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from products.forms import ProductEntryForm
from products.models import Katalog

# Create your views here.
def show_products(request):
    product_entries = Katalog.objects.all()
    context = {
        "product_entries": product_entries
    }

    return render(request, "products.html", context)