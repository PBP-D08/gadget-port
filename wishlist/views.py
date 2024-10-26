import json
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist, WishlistItem
from products.models import Katalog
from cart_checkout.models import CartItem

@login_required
def user_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user).select_related('katalog')

    query = request.GET.get('q')
    categories = request.GET.getlist('category')
    sort_option = request.GET.get('sort')

    # Handle search by product name
    if query:
        wishlist_items = wishlist_items.filter(katalog__name__icontains=query)

    # Filter by categories if specified
    if categories:
        wishlist_items = wishlist_items.filter(katalog__category__in=categories)

    # Handle sorting
    if sort_option == 'price_asc':
        wishlist_items = wishlist_items.order_by('katalog__price')
    elif sort_option == 'price_desc':
        wishlist_items = wishlist_items.order_by('-katalog__price')

    context = {
        'wishlist_items': [item.katalog for item in wishlist_items],
        'selected_categories': categories,
        'selected_sort': sort_option,
    }
    return render(request, 'wishlist.html', context)

@login_required
@csrf_exempt
def toggle_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist, created = WishlistItem.objects.get_or_create(wishlist__user=request.user, katalog=katalog)

    if created:
        message = 'Product added to wishlist.'
        status = 'added'
    else:
        wishlist.delete()
        message = 'Product removed from wishlist.'
        status = 'removed'

    return JsonResponse({'message': message, 'status': status})

@login_required
@csrf_exempt
def add_to_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist, created = WishlistItem.objects.get_or_create(wishlist__user=request.user, katalog=katalog)

    if created:
        return JsonResponse({'message': 'Product added to wishlist.'}, status=201)
    return JsonResponse({'message': 'Product is already in wishlist.'}, status=200)

@login_required
@csrf_exempt
def remove_from_wishlist(request, katalog_id):
    katalog = get_object_or_404(Katalog, id=katalog_id)
    wishlist_item = WishlistItem.objects.filter(wishlist__user=request.user, katalog=katalog).first()

    if wishlist_item:
        wishlist_item.delete()
        return JsonResponse({'message': 'Product removed from wishlist.'}, status=200)
    return JsonResponse({'message': 'Product not found in wishlist.'}, status=404)

@login_required
@csrf_exempt
def move_to_cart(request, wishlist_item_id):
    try:
        # Ambil item wishlist
        wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, wishlist__user=request.user)

        # Ambil produk yang ada di wishlist item
        katalog = wishlist_item.katalog

        # Tambahkan produk ke keranjang, jika sudah ada tambahkan jumlahnya
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            katalog=katalog,
            defaults={'quantity': 1}
        )
        
        if not created:
            # Jika sudah ada di keranjang, tambahkan jumlahnya
            cart_item.quantity += 1
            cart_item.save()

        # Hapus item dari wishlist setelah dipindahkan
        wishlist_item.delete()

        return JsonResponse({'message': 'Item successfully moved to cart.'}, status=200)

    except WishlistItem.DoesNotExist:
        return JsonResponse({'error': 'Item not found in wishlist.'}, status=404)