# user_profile/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import UserProfile
from .forms import UserProfileForm, SubProfileForm
from authentication.models import Profile

@login_required
def view_profile(request):
    # Mendapatkan profil user yang sedang login
    user = get_object_or_404(UserProfile, profile__user=request.user)
    context = {
        'user': user,
        'username' : user.profile.username,
        'full_name' : user.profile.full_name,
        'email' : user.profile.email,
        'alamat' : user.profile.alamat,
    }
    return render(request, 'view_profile.html', context)

@login_required
def edit_profile(request):
    # Mendapatkan profil yang ingin diedit
    user_profile = get_object_or_404(UserProfile, profile__user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile.profile)
        if form.is_valid():
            form.save()
            return redirect('user:view')
    else:
        form = UserProfileForm(instance=user_profile.profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)  # Pastikan mengembalikan respons di sini

@login_required
def add_sub_profile(request):
    # Mengecek apakah user adalah buyer
    if not request.user.profile.is_buyer():
        return HttpResponseForbidden("Only buyers can add sub-profiles.")

    if request.method == 'POST':
        form = SubProfileForm(request.POST)
        if form.is_valid():
            sub_profile = form.save(commit=False)
            # Ambil profil pengguna saat ini
            user_profile = request.user.profile  # Akses profile dari user
            sub_profile.parent_profile = user_profile  # Pastikan ini adalah relasi yang benar
            sub_profile.save()
            return redirect('user:view')
    else:
        form = SubProfileForm()
    
    context = {'form': form}
    return render(request, 'add_sub_profile.html', context)
