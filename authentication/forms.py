from django.contrib.auth.forms import UserCreationForm
from django import forms
from authentication.models import Profile
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(
        choices = (("Admin", "Admin"), ("Buyer", "Buyer")),
        label="Choose your role",
        required=True
    )
    email = forms.EmailField(label="Email", required=True)
    full_name = forms.CharField(label="Name", required=True)
    alamat = forms.CharField(label="Address", required=True)

    class Meta:
        model = User
        fields = ("role", "username", "full_name", "email", "password1", "password2", "alamat")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]  # Save email to the User model

        if commit:
            user.save()

        # Check if Profile already exists for the user to avoid duplication
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                "full_name": self.cleaned_data["full_name"],
                "role": self.cleaned_data["role"],
                "alamat": self.cleaned_data["alamat"],
            }
        )

        return user
