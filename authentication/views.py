# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from authentication.forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import User  # Pastikan untuk mengimpor model User

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            response = HttpResponseRedirect("/")
            response.set_cookie("user_logged_in", str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

@csrf_exempt
def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()  # Simpan pengguna yang baru dibuat
            messages.success(request, 'Your account has been successfully created!')
            return redirect('authentication:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def logout(request):
    auth_logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('user_logged_in')
    return response
