from django import forms


class NameForm(forms.Form):
    data_for_search = forms.CharField(max_length=100,
                                      widget=forms.TextInput(attrs={'placeholder': 'Enter model, manufacturer or id...',
                                                                    'class': 'form-control'}))
