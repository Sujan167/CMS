from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'email', 'first_name', 'last_name']
