from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter model, manufacturer or id...',
                                                              'class': 'form-control'}))
