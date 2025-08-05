from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ClientLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={"autofocus": True}))