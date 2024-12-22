import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, CartItem, Order, Address, ShippingMethod
from review.models import Katalog
from django.contrib import messages
from django.db.models import Sum, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.core import serializers
from django.http import HttpResponse
# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.decorators import action



# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = CartItemSerializer
    
#     def get_queryset(self):
#         return CartItem.objects.filter(user=self.request.user)

#     @action(detail=True, methods=['post'])
#     def toggle_select(self, request, pk=None):
#         cart_item = self.get_object()
#         cart_item.selected = not cart_item.selected
#         cart_item.save()
#         return Response(self.serializer_class(cart_item).data)

#     @action(detail=False, methods=['post'])
#     def select_all(self, request):
#         self.get_queryset().update(selected=True)
#         return Response({'status': 'success'})

#     @action(detail=False, methods=['post'])
#     def unselect_all(self, request):
#         self.get_queryset().update(selected=False)
#         return Response({'status': 'success'})

# ====================================================
#                        Cart
# ====================================================

@login_required
@csrf_exempt
def add_to_cart(request, product_id):
    """Add a product to the user's cart"""
    print("=== Debug Add to Cart ===")
    print(f"Method: {request.method}")
    print(f"Product ID: {product_id}")
    print(f"Request Body: {request.body}")
    
    try:
        # Parse JSON data
        if request.body:
            data = json.loads(request.body)
            quantity = data.get('quantity', 1)
        else:
            quantity = 1
            
        print(f"Quantity: {quantity}")
        
        # Get product from Katalog model
        katalog = Katalog.objects.get(id=product_id)
        print(f"Found Product: {katalog.name}")
        
        # Add to cart using Katalog
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=katalog,  # Gunakan katalog sebagai product
            defaults={'quantity': quantity}
        )
        
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            
        print("Cart item saved successfully")
        
        return JsonResponse({
            'status': 'success',
            'message': 'Product added to cart successfully!',
            'cart_count': CartItem.objects.filter(user=request.user).count()
        })
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': 'Invalid JSON data'
        }, status=400)
        
    except Katalog.DoesNotExist:
        print(f"Product Not Found: ID {product_id}")
        return JsonResponse({
            'status': 'error',
            'message': f'Product with ID {product_id} not found'
        }, status=404)
        
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product', 'product__store')
    total = sum(item.get_total() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart.html', context)

@login_required
@csrf_exempt
def checkout(request):
    """Improved checkout view with proper validation and error handling."""
    cart_items = (CartItem.objects
                    .filter(user=request.user, selected=True)
                    .select_related('product'))
                    
    if not cart_items.exists():
        messages.warning(request, 'Please select items to checkout')
        return redirect('cart_checkout:cart')
        
    addresses = Address.objects.filter(user=request.user)
    items_total = sum((item.get_total() for item in cart_items), Decimal('0'))
    
    context = {
        'cart_items': cart_items,
        'addresses': addresses,
        'default_address': addresses.filter(is_default=True).first(),
        'items_total': items_total,
    }
    return render(request, 'checkout.html', context)

@login_required
@csrf_exempt
def payment(request):
    """Handle payment processing"""
    try:
        order = Order.objects.filter(
            user=request.user,
            status='pending'
        ).select_related('address', 'shipping_method').first()
        
        if not order:
            messages.error(request, 'No pending order found')
            return redirect('cart_checkout:cart')
            
        payment_methods = [
            {'id': 'bank_transfer', 'name': 'Bank Transfer'},
            {'id': 'credit_card', 'name': 'Credit Card'},
            {'id': 'ewallet', 'name': 'E-Wallet'}
        ]
        
        context = {
            'order': order,
            'payment_methods': payment_methods
        }
        
        return render(request, 'payments.html', context)
        
    except Exception as e:
        messages.error(request, 'Error processing payment')
        return redirect('cart_checkout:checkout')

@login_required
@csrf_exempt
def confirm_order(request):
    """Confirm and finalize the order"""
    try:
        order = get_object_or_404(
            Order,
            id=request.POST.get('order_id'),
            user=request.user,
            status='pending'
        )
        
        payment_method = request.POST.get('payment_method')
        payment_details = request.POST.get('payment_details')
        
        if not all([payment_method, payment_details]):
            messages.error(request, 'Please provide payment information')
            return redirect('cart_checkout:payment')
            
        order.status = 'confirmed'
        order.payment_method = payment_method
        order.payment_details = payment_details
        order.save()
        
        CartItem.objects.filter(user=request.user).delete()
        
        context = {
            'order': order,
            'success_message': 'Order confirmed successfully!'
        }
        
        return render(request, 'order_confirmation.html', context)
        
    except Order.DoesNotExist:
        messages.error(request, 'Order not found')
        return redirect('cart_checkout:cart')
    except Exception as e:
        messages.error(request, 'Error confirming order')
        return redirect('cart_checkout:payment')

def calculate_cart_total(user):
    """Helper function to calculate cart total"""
    cart_items = CartItem.objects.filter(user=user)
    return sum(item.get_total() for item in cart_items)

# ====================================================
#                      Checkout
# ====================================================

@login_required
@csrf_exempt
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user, selected=True)
    if not cart_items.exists():
        return redirect('cart_checkout:cart')
    
    addresses = Address.objects.filter(user=request.user)
    default_address = addresses.filter(is_default=True).first()
    
    items_total = sum(item.get_total() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'addresses': addresses,
        'default_address': default_address,
        'items_total': items_total,
    }
    return render(request, 'checkout.html', context)

@login_required
@csrf_exempt
def update_address(request):
    if request.method == 'POST':
        address_id = request.POST.get('address_id')
        address = Address.objects.get(id=address_id, user=request.user)
        
        Address.objects.filter(user=request.user).update(is_default=False)
        address.is_default = True
        address.save()
        
        return JsonResponse({'status': 'success'})

@login_required
@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user, selected=True)
        address = Address.objects.get(id=request.POST.get('address_id'))
        shipping_method = ShippingMethod.objects.get(id=request.POST.get('shipping_method_id'))
        donation = request.POST.get('donation', 0)
        
        items_total = sum(item.get_total() for item in cart_items)
        grand_total = items_total + shipping_method.price + Decimal(donation)
        
        order = Order.objects.create(
            user=request.user,
            address=address,
            shipping_method=shipping_method,
            items_total=items_total,
            shipping_total=shipping_method.price,
            donation=donation,
            grand_total=grand_total
        )
        
        cart_items.delete()
        
        return JsonResponse({'status': 'success', 'order_id': order.id})

def get_json_cart(request):
    # Get all cart items for current user
    data = CartItem.objects.filter(user=request.user)
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_json_cart(request):
    # Get all cart items with related product data
    data = CartItem.objects.select_related('product').filter(user=request.user)
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

@login_required
@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            action = data.get('action')
            
            if not item_id or not action:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Missing item_id or action'
                }, status=400)

            try:
                cart_item = CartItem.objects.get(id=item_id, user=request.user)
            except CartItem.DoesNotExist:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Cart item not found'
                }, status=404)
            
            if action == 'increment':
                cart_item.quantity += 1
                cart_item.save()
            elif action == 'decrement':
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                else:
                    cart_item.delete()
                    return JsonResponse({
                        'status': 'success',
                        'message': 'Item removed',
                        'quantity': 0,
                        'total': calculate_cart_total(request.user),
                        'item_count': CartItem.objects.filter(user=request.user).count()
                    })
            elif action == 'remove':
                cart_item.delete()
                return JsonResponse({
                    'status': 'success',
                    'message': 'Item removed',
                    'quantity': 0,
                    'total': calculate_cart_total(request.user),
                    'item_count': CartItem.objects.filter(user=request.user).count()
                })
            elif action in ['select', 'unselect']:
                cart_item.selected = (action == 'select')
                cart_item.save()
            
            return JsonResponse({
                'status': 'success',
                'quantity': cart_item.quantity,
                'total': calculate_cart_total(request.user),
                'item_count': CartItem.objects.filter(user=request.user).count()
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid JSON data'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=405)