from django.shortcuts import render

<<<<<<< HEAD
def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

=======
# Create your views here.
def show_main(request):
    context = {"user": request.user}
>>>>>>> 0c5a246f8520adb78d961c4a79d5d6a761a164f1
    return render(request, "main.html", context)