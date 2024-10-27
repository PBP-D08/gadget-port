from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StoreForm
from .models import Store
from authentication.models import Profile
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound

@login_required(login_url="authentication:login")
def list_store(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)

    if user_profile.role.casefold() == "admin":
        store_list = serializers.serialize('json', Store.objects.all())
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
    context = {'store': store}
    if Profile.objects.get(user=request.user).role.casefold() == "admin":
        return render(request, 'admin_store_detail.html', context)
    return render(request, 'store_detail.html', context)