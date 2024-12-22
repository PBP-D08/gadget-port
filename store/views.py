import base64
import datetime
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import StoreForm
from .models import Store
from authentication.models import User
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from products.models import Katalog
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

@login_required(login_url="authentication:login")
def list_store(request):
    if request.user.role == "admin":
        store_list = serializers.serialize('json', Store.objects.filter(user=request.user))
        store_list = serializers.deserialize('json', store_list)
        store_list = [store.object for store in store_list]

        return render(request, 'admin_store.html', {'store_list': store_list})

    store_list = Store.objects.all()
    context = {
        'store_list': store_list,
    }

    return render(request, 'store.html', context)


@login_required(login_url="authentication:login")
def add_store(request):
    if request.method == "POST":
        nama = request.POST.get('nama')
        alamat = request.POST.get('alamat')
        jam_buka = request.POST.get('jam_buka')
        jam_tutup = request.POST.get('jam_tutup')
        nomor_telepon = request.POST.get('nomor_telepon')
        logo = request.FILES.get("logo")

        new_store = Store(nama=nama, alamat=alamat,jam_buka=jam_buka, 
                           jam_tutup=jam_tutup, nomor_telepon=nomor_telepon, logo=logo, user=request.user)
        new_store.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url="authentication:login")
def edit_store(request, id):
    store = Store.objects.get(pk = id)
    form = StoreForm(request.POST or None, request.FILES or None, instance=store)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse("store:list_store"))

    context = {"form": form}
    return render(request, "edit_store.html", context)


@login_required(login_url="authentication:login")
def delete_store(request, id):
    store = Store.objects.get(pk = id)
    store.delete()
    return HttpResponseRedirect(reverse('store:list_store'))

@login_required(login_url="authentication:login")
def store_detail(request, id):
    store = get_object_or_404(Store, id=id)
    products = Katalog.objects.filter(store=store)
    context = {'store': store, 'products': products}
    if request.user.role == "admin":
        return render(request, 'admin_store_detail.html', context)
    return render(request, 'store_detail.html', context)

def show_json_store(request):
    # Ambil semua data Store
    data = Store.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def get_store_json(request):
    stores = Store.objects.all()

    data = []
    for store in stores:
        data.append({
            "model": "store.store",
            "pk": store.id,
            "fields": {
                "user": store.user.id,
                "nama": store.nama or "Unknown Store",
                "alamat": store.alamat or "No address available",
                "nomor_telepon": store.nomor_telepon or "",
                "logo": request.build_absolute_uri(store.logo.url) if store.logo else "",
                "jam_buka": str(store.jam_buka) if store.jam_buka else "00:00:00",
                "jam_tutup": str(store.jam_tutup) if store.jam_tutup else "00:00:00",
            },          
        })
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_store_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

         # Decode base64 menjadi file
        logo_data = data.get("logo")
        if not logo_data:
            return JsonResponse({"status": "error", "message": "Logo is required"}, status=400)

        try:
            format, imgstr = logo_data.split(';base64,')
            ext = format.split('/')[-1]
            logo_file = ContentFile(base64.b64decode(imgstr), name=f"logo.{ext}")
        except Exception:
            return JsonResponse({"status": "error", "message": "Invalid logo format"}, status=400)
        
        store = Store.objects.create(
            user=request.user,
            nama=data['nama'],
            alamat=data['alamat'],
            jam_buka=data['jam_buka'],
            jam_tutup=data['jam_tutup'],
            nomor_telepon=data['nomor_telepon'],
            logo=logo_file,  # Pass the converted file
        )

        store.save()

        return JsonResponse({
            "status": "success",
            "message": "Store created successfully"
        }, status=200)
        
    
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    }, status=401)

@csrf_exempt
def edit_store_flutter(request, store_id):
    if request.method == 'POST' or request.method == 'PUT':
        try:
            data = json.loads(request.body)
            store = Store.objects.get(pk=store_id)
            
            store.nama = data['nama']
            store.alamat = data['alamat']
            store.nomor_telepon = data['nomor_telepon']
            
            store.save()
            
            return JsonResponse({"status": "success"}, status=200)
        except Store.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Store not found"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    elif request.method == 'GET':
        try:
            store = Store.objects.get(pk=store_id)
            return JsonResponse({
                "status": "success",
                "data": {
                    "nama": store.nama or "Unknown Store",
                    "alamat": store.alamat or "No address available",
                    "nomor_telepon": store.nomor_telepon or "",
                }
            })
        except Store.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Store not found"}, status=404)
    
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def delete_store_flutter(request, id):
    if request.method == 'DELETE':
        review = get_object_or_404(Store, id=id)
        review.delete()
        return JsonResponse({'message': 'Store deleted successfully!'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_product_by_id(request, id):
    store = get_object_or_404(Store, id=id)
    products = Katalog.objects.filter(store=store)
    return HttpResponse(serializers.serialize("json", products), content_type="application/json")
