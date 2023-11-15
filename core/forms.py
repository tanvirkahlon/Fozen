from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'YOUR USERNAME',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'YOUR PASSWORD',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'YOUR USERNAME',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'YOUR EMAIL',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'YOUR PASSWORD',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'REPEAT YOUR PASSWORD',
        'class': 'w-full py-4 px-6 rounded-xl text-xs'
    }))