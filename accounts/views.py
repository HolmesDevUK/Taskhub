from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forms import LoginForm

class LoginView(LoginView):
    authentication_form = LoginForm
    template_name = "accounts/login.html"

# Create your views here.
