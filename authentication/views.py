# authentication/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from authentication.forms import RegisterForm
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import datetime, json
from .models import User  # Pastikan untuk mengimpor model User

@csrf_exempt
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
def login_flutter(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        # Authenticate user
        user = authenticate(username=username, password=password)
        print(user.id)
        if user is not None:
            if user.is_active:
                print(user.is_admin)
                print(user.role)
                                # Login user
                auth_login(request, user)
                # Return JSON response on successful login
                if user.role == 'admin' :
                    return JsonResponse({
                        "username": user.username,
                        "status": True,
                        "message": "Login sukses!",
                        "role" : 'admin',
                        "userId" : user.id
                    }, status=200)
                else:
                    return JsonResponse({
                        "username": user.username,
                        "status": True,
                        "message": "Login sukses!",
                        "role" : 'buyer',
                        "userId" : user.id
                    }, status=200)
            else:
                # User account is inactive
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=401)
        else:
            # Authentication failed
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali username atau kata sandi."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Metode tidak didukung."
        }, status=405)
    
@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        try:
            # Parse request body
            data = json.loads(request.body)

            # Extract fields
            role = data.get('role', 'buyer')  # Default role is 'buyer'
            username = data.get('username')
            full_name = data.get('full_name')
            email = data.get('email')
            password1 = data.get('password1')
            password2 = data.get('password2')

            # Validate required fields
            if not all([role, username, full_name, email, password1, password2]):
                return JsonResponse({
                    "status": False,
                    "message": "All fields are required."
                }, status=400)

            # Validate passwords
            if password1 != password2:
                return JsonResponse({
                    "status": False,
                    "message": "Passwords do not match."
                }, status=400)

            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Username already exists."
                }, status=400)

            # Check if the email is already used
            if User.objects.filter(email=email).exists():
                return JsonResponse({
                    "status": False,
                    "message": "Email already exists."
                }, status=400)

            # Create the new user
            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=full_name.split(" ")[0],  # Extract first name
                last_name=" ".join(full_name.split(" ")[1:]),  # Extract last name
                role=role
            )
            user.full_name = full_name  # Assign full_name explicitly if needed
            user.save()

            return JsonResponse({
                "username": user.username,
                "status": 'success',
                "message": "User created successfully!"
            }, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({
                "status": False,
                "message": "Invalid JSON format."
            }, status=400)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)

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