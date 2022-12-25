from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Model
from django.forms import BooleanField


class SearchForm(forms.Form):
    pass


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=250, help_text='eg youremail@gmail.com')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class Settings(Model):
    receive_newsletter = BooleanField()


class SettingsForm(forms.ModelForm):

    # receive_newsletter = forms.BooleanField()
    # receive_newsletter2 = forms.BooleanField()
    # receive_newsletter3 = forms.BooleanField()
    # receive_newsletter4 = forms.BooleanField()


    # def __init__(self):
    #     self.fields['receive_newsletter'].initial = True

    class Meta:
        model = Settings
        fields = '__all__'