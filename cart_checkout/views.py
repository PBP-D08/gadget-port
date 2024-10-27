from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, CartItem, Order, Address, ShippingMethod
from django.contrib import messages
from django.db.models import Sum, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal

# ====================================================
#                        Cart
# ====================================================

@login_required
@csrf_exempt
def add_to_cart(request, product_id):
    """Add a product to the user's cart"""
    try:
        product = get_object_or_404(Product, id=product_id)
        print(product)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
            
        messages.success(request, 'Product added to cart successfully!')
        return redirect('cart_checkout:cart')
        
    except Exception as e:
        messages.error(request, 'Error adding product to cart')
        return redirect('cart.html', product_id=product_id)

@login_required
@csrf_exempt
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product', 'product__store')
    return render(request, 'cart.html', {'cart_items': cart_items})

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

def calculate_order_total(cart_items, shipping_method=None, donation=Decimal('0.00')):
    """Calculate the total order amount including shipping and donation"""
    subtotal = sum(item.get_total() for item in cart_items)
    shipping_cost = shipping_method.price if shipping_method else Decimal('0.00')
    
    return subtotal + shipping_cost + donation

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
