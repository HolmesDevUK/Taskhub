from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import ClientRequiredMixin
from django.views.generic import ListView

from core.models import Task

# Create your views here.

class DashboardView(LoginRequiredMixin, ClientRequiredMixin, ListView):
    model = Task
    template_name = "clients/dashboard.html"
