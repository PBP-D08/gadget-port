from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from authentication.models import User
from cart_checkout.models import Order
from django.http import JsonResponse
from django.core import serializers

@login_required
def view_profile(request):
    # Get the logged-in user's profile
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    # Fetch the checkout history
    orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

    context = {
        'user_profile' : user_profile,
        'orders': orders,  # Add order history
    }
    return render(request, 'view_profile.html', context)

@login_required
def edit_profile(request):
    # Get the profile to edit
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile.user)  # Use user here
        if form.is_valid():
            form.save()
            return redirect('user:view_profile')
    else:
        form = UserProfileForm(instance=user_profile.user)  # Use user here

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

@login_required
def add_bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        user = get_object_or_404(User, id=request.user.id)  # Correctly get user
        user.bio = bio
        user.save()
        return redirect('user:view_profile')
    
    return render(request, 'add_bio.html', {'user': request.user})

@login_required
def edit_bio(request):
    user = get_object_or_404(User, id=request.user.id)  # Correctly get user

    if request.method == 'POST':
        bio = request.POST.get('bio')
        user.bio = bio
        user.save()
        return redirect('user:view_profile')

    context = {'bio': user.bio}
    return render(request, 'edit_bio.html', context)

@login_required
def delete_bio(request):
    user = get_object_or_404(User, id=request.user.id)  # Correctly get user
    user.bio = ''
    user.save()
    return redirect('user:view_profile')

@login_required
def checkout_history(request):
    """View to display the user's checkout history"""
    orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

    return render(request, 'checkout_history.html', {'orders': orders})

def show_json(request):
    # Mengambil semua data dari model UserProfile
    data = UserProfile.objects.all()
    
    # Serialisasi data ke dalam format JSON
    serialized_data = serializers.serialize('json', data)
    return JsonResponse(serialized_data, safe=False)