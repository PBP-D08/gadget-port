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

from django.http import JsonResponse
from django.core import serializers
from .models import UserProfile

def show_json(request):
    # Mengambil data dari UserProfile dan menyertakan semua field dari User
    data = UserProfile.objects.select_related('user').values(
        'id', 
        'user_id',
        # 'user__password',        # Menyertakan password
        'user__last_login',      # Menyertakan last_login
        # 'user__is_superuser',    # Menyertakan is_superuser
        'user__username',        # Menyertakan username
        'user__first_name',      # Menyertakan first_name
        # 'user__last_name',       # Menyertakan last_name
        'user__email',           # Menyertakan email
        'user__bio',             # bio juga
        # 'user__is_staff',        # Menyertakan is_staff
        # 'user__is_active',       # Menyertakan is_active
        # 'user__date_joined',     # Menyertakan date_joined
        'user__full_name',       # Menyertakan full_name
        'user__role',            # Menyertakan role
        'user__alamat',          # Menyertakan alamat
        # 'user__groups',          # Menyertakan groups
        # 'user__user_permissions', # Menyertakan user_permissions
        # 'parent_profile_id'      # Menyertakan parent_profile_id
    )

    # Mengembalikan data JSON
    return JsonResponse(list(data), safe=False, json_dumps_params={'indent': 4})

@csrf_exempt
@login_required
def view_profile_flutter(request):
    if request.method == 'GET':
        # Get the user's profile
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Get the user's orders
        orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

        user_profile_data = {
            'user_profile': {
                'id': user_profile.id,
                'user_id': user_profile.user.id,
                'username': user_profile.user.username,
                'first_name': user_profile.user.first_name,
                'email': user_profile.user.email,
                'bio': user_profile.user.bio,
            },
            'orders': list(orders.values())
        }

        return JsonResponse(user_profile_data, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)
    
@csrf_exempt
@login_required
def edit_profile_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_profile = UserProfile.objects.get(user=request.user)
        
        # Assuming you're updating the user fields like username, email, etc.
        user_profile.user.username = data.get('username', user_profile.user.username)
        user_profile.user.email = data.get('email', user_profile.user.email)
        user_profile.user.first_name = data.get('first_name', user_profile.user.first_name)
        user_profile.user.save()

        user_profile.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@csrf_exempt
@login_required
def add_bio_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bio = data.get('bio', '')

        user = request.user
        user.bio = bio
        user.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@csrf_exempt
@login_required
def edit_bio_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bio = data.get('bio', '')

        user = request.user
        user.bio = bio
        user.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@csrf_exempt
@login_required
def delete_bio_flutter(request):
    if request.method == 'POST':
        user = request.user
        user.bio = ''
        user.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

@csrf_exempt
@login_required
def checkout_history_flutter(request):
    if request.method == 'GET':
        orders = Order.objects.filter(user=request.user).select_related('address', 'shipping_method')

        orders_data = list(orders.values('id', 'status', 'total_price', 'shipping_method__name', 'address__city'))
        return JsonResponse({"orders": orders_data}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)
