from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import AdminRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from accounts.models import CustomUser
from .forms import CreateClientForm

# Create your views here.

class DashboardView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = CustomUser
    template_name = "adminpanel/dashboard.html"

class CreateClientView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = CustomUser
    form_class = CreateClientForm
    template_name = 'adminpanel/create_client.html'
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = 'client'
        user.first_login = True

        random_password = CustomUser.objects.make_random_password()
        user.set_password(random_password)
        user.save()

        return super().form_valid(form)
    
