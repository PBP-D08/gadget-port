import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Wishlist
from products.models import Katalog
# from cart_checkout.models import CartItem
# from cart_checkout.models import Product, Store, CartItem

@login_required
def user_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')

    query = request.GET.get('q')
    categories = request.GET.getlist('category')
    sort_option = request.GET.get('sort')

    # Handle search by product name
    if query:
        wishlist_items = wishlist_items.filter(product__name__icontains=query)

    # Filter by categories if specified
    if categories:
        wishlist_items = wishlist_items.filter(product__category__in=categories)

    # Handle sorting
    if sort_option == 'price_asc':
        wishlist_items = wishlist_items.order_by('product__price')
    elif sort_option == 'price_desc':
        wishlist_items = wishlist_items.order_by('-product__price')

    context = {
        'wishlist_items': wishlist_items,  # No need to extract products, template can access through item.product
        'categories': Katalog.CATEGORY_CHOICES,
        'selected_categories': categories,
        'selected_sort': sort_option,
    }
    return render(request, 'wishlist.html', context)

@login_required
@csrf_exempt
def add_to_wishlist(request, katalog_id):
    try:
        product = get_object_or_404(Katalog, id=katalog_id)
        wishlist, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            message = 'Berhasil ditambahkan ke wishlist!' if created else 'Berhasil dihapus dari wishlist!'
            status = 'added' if created else 'removed'
            return JsonResponse({
                'message': message,
                'status': status
            }, status=200)
        
        return redirect('wishlist:user_wishlist')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'message': f'Terjadi kesalahan: {str(e)}',
                'status': 'error'
            }, status=500)
        return redirect('wishlist:user_wishlist')
    
@login_required
@csrf_exempt
def remove_from_wishlist(request, katalog_id):
    try:
        wishlist_item = Wishlist.objects.get(
            user=request.user,
            product_id=katalog_id
        )
        wishlist_item.delete()
        return JsonResponse({
            'message': 'Berhasil dihapus dari wishlist.',
            'status': 'success'
        }, status=200)
    except Wishlist.DoesNotExist:
        return JsonResponse({
            'message': 'Item tidak ditemukan di wishlist.',
            'status': 'error'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'message': f'Terjadi kesalahan: {str(e)}',
            'status': 'error'
        }, status=500)

# @login_required
# @csrf_exempt
# def move_to_cart(request, wishlist_item_id):
#     try:
#         # Ambil wishlist item
#         wishlist_item = get_object_or_404(Wishlist, id=wishlist_item_id, user=request.user)
        
#         # Cari atau buat Product yang sesuai dengan Katalog
#         product, created = Product.objects.get_or_create(
#             name=wishlist_item.product.name,
#             defaults={
#                 'store': Store.objects.first(),  # Sesuaikan dengan store yang sesuai
#                 'description': wishlist_item.product.description,
#                 'price': wishlist_item.product.price,
#                 'original_price': wishlist_item.product.price,
#                 'image': wishlist_item.product.image
#             }
#         )
        
#         # Tambahkan ke cart
#         cart_item, created = CartItem.objects.get_or_create(
#             user=request.user,
#             product=product,
#             defaults={'quantity': 1}
#         )
        
#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()
        
#         # Hapus dari wishlist
#         wishlist_item.delete()
        
#         return JsonResponse({
#             'message': 'Item berhasil dipindahkan ke keranjang.',
#             'status': 'success'
#         })
        
#     except Exception as e:
#         print(f"Error detail: {str(e)}")
#         return JsonResponse({
#             'message': f'Terjadi kesalahan: {str(e)}',
#             'status': 'error'
#         }, status=500)