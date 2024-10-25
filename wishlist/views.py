import json
from django.shortcuts import get_object_or_404, render, redirect

from products.models import Katalog
from .models import Wishlist, WishlistItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from authentication.models import Profile  # Import Profile model

def roler(request):
    # Mengambil profile dari user yang terotentikasi
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    role = 'none'
    if profile.role == "Buyer":
        role = 'buyer'
    elif profile.role == "Admin":
        role = 'admin'
    return role

@login_required
def user_wishlist(request):
    user = request.user
    user_wishlisted = None
    role = None

    if user.is_authenticated:
        # Ambil profile user
        profile = get_object_or_404(Profile, user=user)
        user_wishlisted = Wishlist.objects.filter(user=user)
        # Filter item yang belum dibeli
        wishlist_items = WishlistItem.objects.filter(wishlist__in=user_wishlisted, is_purchased=False)
        role = roler(request)  # Tentukan role berdasarkan profile user
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items, 'role': role})

def get_wishlist_json(request):
    wishlist_item = Wishlist.objects.all()
    return HttpResponse(serializers.serialize('json', wishlist_item))

@login_required
@csrf_exempt  # Disable CSRF only if necessary (we use CSRF token in JS)
def add_wishlist(request):
    if request.method == 'POST':
        user = request.user
        try:
            data = json.loads(request.body)
            product_name = data.get("name")

            # Cek apakah produk sudah ada di wishlist
            existing_wishlist = Wishlist.objects.filter(user=user, name=product_name)
            if existing_wishlist.exists():
                return JsonResponse({'message': 'Item already in wishlist.'}, status=409)

            # Tambahkan produk ke wishlist
            Wishlist.objects.create(user=user, name=product_name)
            return JsonResponse({'message': 'Item added to wishlist.'}, status=201)

        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@login_required
@require_POST
@csrf_protect
def delete_wishlist(request, katalog_id):
    try:
        katalog = WishlistItem.objects.get(id=katalog_id)

        # Hanya izinkan user yang membuat wishlist untuk menghapus itemnya
        if katalog.wishlist.user == request.user:
            katalog.delete()
            return JsonResponse({'message': 'Item successfully removed from wishlist.'}, status=200)
        else:
            return JsonResponse({'error': 'Permission denied.'}, status=403)

    except WishlistItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found.'}, status=404)

def view_json_wishlist(request):
    user = request.user
    data = Wishlist.objects.filter(user=user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_wishlist_katalog(request):
    user = request.user
    user_wishlisted = Wishlist.objects.filter(user=user)
    data = WishlistItem.objects.filter(wishlist__in=user_wishlisted)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def view_json_wishlist_katalog_id(request, id):
    user = request.user
    try:
        wishlist = Wishlist.objects.get(user=user, id=id)
        data = WishlistItem.objects.filter(wishlist=wishlist)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    except Wishlist.DoesNotExist:
        return HttpResponseNotFound("Wishlist not found")
