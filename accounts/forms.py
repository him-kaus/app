from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):  # Modelform for registration
    username = forms.CharField(max_length=123, required=True)
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "is_active")

class MySignInForm(AuthenticationForm):  # Modelform for registration
    username = forms.CharField(max_length=123, required=True)
    password = forms.CharField(label="Password")
