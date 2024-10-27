import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import  Katalog
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from store.models import Store
from products.forms import ProductEntryForm


# Create your views here.
@login_required(login_url="authentication:login")
def show_products(request):

    # Cek apakah ada query untuk filter atau sort
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    sort_option = request.GET.get('sort')

    # Filter produk jika ada parameter yang diberikan
    if category or brand or sort_option:
        products = get_filtered_products(request)  # Memanggil fungsi filter
    else:
        # Jika tidak ada filter, ambil semua produk
        products = serializers.serialize('json', Katalog.objects.all())
        products = serializers.deserialize('json', products)
        products = [product.object for product in products]

    # Render template yang sesuai berdasarkan role pengguna
    stores = Store.objects.filter(user=request.user)
    if request.user.role == "admin":
        return render(request, 'admin_products.html', {'products': products, 'store': stores})

    return render(request, 'products.html', {'products': products, 'store': stores})

def get_filtered_products(request):
    # Ambil semua data dari Katalog
    products = Katalog.objects.all()

    # Ambil parameter filter dari query string
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    sort_option = request.GET.get('sort')

    # Filter berdasarkan kategori jika ada
    if category:
        products = products.filter(category=category)

    # Filter berdasarkan brand jika ada
    if brand:
        products = products.filter(brand=brand)

    # Sorting berdasarkan opsi yang diberikan
    if sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')

    return products

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        spec = request.POST.get('spec')
        image_link = request.POST.get('image_link')
        store_id = request.POST.get('store')
        store = Store.objects.get(id=store_id)

        new_product = Katalog(category=category, name=name, brand=brand,
                           price=price, spec=spec, image_link=image_link, store=store)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url="authentication:login")
def edit_product(request, id):
    product = Katalog.objects.get(pk=id)
    store = Store.objects.filter(user=request.user)
    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products:show_products")
    else:
        form = ProductEntryForm(instance=product)

    context = {
        "form": form,
        "product": product,
        "store": store,
    }
    return render(request, "edit_product.html", context)

@login_required(login_url="login")
def delete_product(request, id):
    product = Katalog.objects.get(pk=id)
    product.delete()
    return redirect("products:show_products")

def get_product(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")