from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Pengguna

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]

        labels = {
            'username':'Username For Login',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password',
        }

        widgets = {
            'username':TextInput,
            'email':EmailInput(
                attrs={
                    'type':'email',
                    'placeholder':'xx@gg.cc'
                }
            ),
        }

class PenggunaForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = '__all__'
        exclude = ['user']
