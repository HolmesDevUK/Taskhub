from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.mixins import BootstrapFormMixin

class LoginForm(BootstrapFormMixin, AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={"autofocus": True}))