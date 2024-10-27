from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["role", "username", "full_name", "email", "password1", "password2"]
