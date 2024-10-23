from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }
    return render(request, "main.html", context)
    
# # Create your views here.
# def show_main(request):
#     context = {"user": request.user}

@login_required
def add_to_cart(request, product_id):
    return redirect('cart')

@login_required
def cart_view(request):
    return render(request, 'cart.html', {''})

@login_required
def checkout(request):
    return render(request, 'checkout.html', )

@login_required
def payment(request):
    return render(request, 'payment.html')

# @login_required
# def confirm_order(request):
#     order = get_object_or_404()
#     return render(request)

