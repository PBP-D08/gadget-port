from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from authentication.models import User
from cart_checkout.models import Order  # Ensure you import the Order model

@login_required
def view_profile(request):
    # Get the logged-in user's profile
    user = get_object_or_404(UserProfile, profile__user=request.user)

    # Fetch the checkout history
    orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

    context = {
        'user': user,
        'username': user.profile.username,
        'full_name': user.profile.full_name,
        'email': user.profile.email,
        'alamat': user.profile.alamat,
        'orders': orders,  # Add order history
    }
    return render(request, 'view_profile.html', context)

@login_required
def edit_profile(request):
    # Get the profile to edit
    user_profile = get_object_or_404(UserProfile, profile__user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile.profile)
        if form.is_valid():
            form.save()
            return redirect('user:view_profile')  # Change to 'user:view_profile'
    else:
        form = UserProfileForm(instance=user_profile.profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

@login_required
def add_bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile = get_object_or_404(User, user=request.user)
        profile.bio = bio
        profile.save()
        return redirect('user:view_profile')  # Change to 'user:view_profile'
    
    return render(request, 'add_bio.html', {'user': request.user})

@login_required
def edit_bio(request):
    profile = get_object_or_404(User, user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile.bio = bio
        profile.save()
        return redirect('user:view_profile')  # Change to 'user:view_profile'

    context = {'bio': profile.bio}
    return render(request, 'edit_bio.html', context)

@login_required
def delete_bio(request):
    profile = get_object_or_404(User, user=request.user)
    profile.bio = ''
    profile.save()
    return redirect('user:view_profile')  # Change to 'user:view_profile'

@login_required
def checkout_history(request):
    """View to display the user's checkout history"""
    orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

    return render(request, 'checkout_history.html', {'orders': orders})
