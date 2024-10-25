import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import  Katalog
from authentication.models import Profile
from django.contrib.auth.decorators import login_required
# from .forms import BookFilterForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url="authentication:login")
def show_products(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)

    if user_profile.role.casefold() == "admin":
        katalog_list = serializers.serialize('json', Katalog.objects.all())
        katalog_list = serializers.deserialize('json', katalog_list)
        katalog_list = [product.object for product in katalog_list]

        return render(request, 'admin_products.html', {'products': katalog_list})

    products = Katalog.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'products.html', context)

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        spec = request.POST.get('spec')
        image_link = request.POST.get('image_link')

        new_product = Katalog(category=category, name=name, brand=brand,
                           price=price, spec=spec, image_link=image_link)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def get_product(request):
    data = Katalog.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_by_id(request, id):
    data = Katalog.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")