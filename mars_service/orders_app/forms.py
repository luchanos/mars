from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=250, help_text='eg youremail@gmail.com')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
