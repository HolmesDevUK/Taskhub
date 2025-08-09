from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import AdminRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

from accounts.models import CustomUser
from .forms import CreateClientForm
from core.utils import temp_password_generator

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

        random_password = temp_password_generator()
        user.set_password(random_password)
        user.save()

        form_email = form.cleaned_data["email"]
        form_name = form.cleaned_data["name"]

        email = EmailMessage (
            subject= "New TaskHub account",
            body=f"Hello {form_name}, an account has been created for you. \n\n Your email is: {form_email} \n Your password is {random_password}. \n\n You will be prompted to change your password on your first login.",
            from_email= settings.EMAIL_DISPLAY,
            to=[form_email],
        )

        messages.success(
            self.request,
            f"Client {form_name} created Successfully!"
            f"Email: {form_email} | Password: {random_password}"
            "An email has been sent to the client providing their login details."
        )

        email.send()

        return super().form_valid(form)
    
