from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')