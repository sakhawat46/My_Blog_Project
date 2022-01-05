from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields, models
from login_app.models import UserLogin

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['profile_pic', ]
        