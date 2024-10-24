# models.py
from django.db import models
from django.contrib.auth.models import User

# ============================================================
#                       Cart Functions
# ============================================================

class Store(models.Model):
    name = models.CharField(max_length=100)
    # logo = models.ImageField(upload_to='store_logos/')
    is_official = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    selected = models.BooleanField(default=True)

    def get_total(self):
        return self.product.price * self.quantity

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import CartItem, Product

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product', 'product__store')
    return render(request, 'cart.html', {'cart_items': cart_items})

def update_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        
        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        elif action == 'remove':
            cart_item.delete()
            return JsonResponse({'status': 'removed'})
        
        cart_item.save()
        return JsonResponse({
            'status': 'updated',
            'quantity': cart_item.quantity,
            'total': float(cart_item.get_total())
        })
    
# ==================================================================
#                           Checkout
# ==================================================================

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    full_address = models.TextField()
    rt_rw = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.recipient_name} - {self.district}"

class ShippingMethod(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_days = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    shipping_method = models.ForeignKey(ShippingMethod, on_delete=models.SET_NULL, null=True)
    items_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_total = models.DecimalField(max_digits=10, decimal_places=2)
    donation = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"