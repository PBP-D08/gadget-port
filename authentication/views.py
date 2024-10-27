# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from authentication.forms import RegisterForm
from .models import Profile  # Pastikan untuk mengimpor model Profile

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_page = request.GET.get("next")
            if next_page is None:
                response = redirect("main:show_main")
            else:
                response = redirect(next_page)
            response.set_cookie("user_logged_in", user)
            return response
        else:
            messages.error(request, "Sorry, incorrect username or password. Please try again.")
    
    context = {}
    if request.user.is_authenticated:
        return redirect('main:show_main')
    else:
        return render(request, "login.html", context)

@csrf_exempt
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()  # Simpan pengguna yang baru dibuat

            # Buat profil untuk pengguna
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    "full_name": form.cleaned_data['full_name'],
                    "role": form.cleaned_data['role'],
                    "email": user.email,  # Menyimpan email di profil
                    "alamat": form.cleaned_data.get('alamat', '') 
                }
            )

            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def logout(request):
    auth_logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('user_logged_in')
    return response
