from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, CheckboxInput
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Search'}),
            'email': forms.TextInput(attrs={'placeholder': 'Search'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Search'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Search'}),
            'is_active': forms.CheckboxInput(),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

