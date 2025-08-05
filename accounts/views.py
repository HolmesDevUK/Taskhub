from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forms import ClientLoginForm

class ClientLoginView(LoginView):
    authentication_form = ClientLoginForm
    template_name = "accounts/login.html"

# Create your views here.
