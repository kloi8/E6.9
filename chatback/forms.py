from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']


class AccUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']
