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


