from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email*',
        # 'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='Email')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'username*',
    }), label='Username')

    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'first name*',
    # }), label='First Name')
    #
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'last name*',
    # }), label='Last Name')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'password*',
    }), label='Password')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'confirm password*',
    }), label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'email*',
        # 'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='Email')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        # 'placeholder': 'username*',
    }), label='Username')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']