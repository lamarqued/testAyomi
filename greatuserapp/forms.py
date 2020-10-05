from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }

        fields = (
            'email',
        )