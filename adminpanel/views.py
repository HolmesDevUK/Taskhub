from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import AdminRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from accounts.models import CustomUser
from core.models import Task
from .forms import CreateClientForm, CreateTaskForm
from core.utils import temp_password_generator, send_notification

# Create your views here.

class DashboardView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = CustomUser
    template_name = "adminpanel/dashboard.html"

class CreateClientView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = CustomUser
    form_class = CreateClientForm
    template_name = 'adminpanel/create_client.html'
    success_url = reverse_lazy("adminpanel:dashboard")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.role = 'client'
        user.first_login = True

        random_password = temp_password_generator()
        user.set_password(random_password)
        user.save()

        form_email = form.cleaned_data["email"]
        form_name = form.cleaned_data["name"]

        send_notification (
            subject = "New TaskHub account",
            message = f"Hello {form_name}, an account has been created for you. \n\n Your email is: {form_email} \n Your password is {random_password}. \n\n You will be prompted to change your password on your first login.",
            to_email = [form_email],
        )

        messages.success(
            self.request,
            f"Client {form_name} created Successfully!"
            f"Email: {form_email} | Password: {random_password}"
            "An email has been sent to the client providing their login details."
        )

        return super().form_valid(form)
    

    class CreateTaskView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
        model = Task
        form_class = CreateTaskForm
        template_name = 'adminpanel/create_task.html'
        success_url = reverse_lazy("adminpanel:dashboard")
    
