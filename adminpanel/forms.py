from django import forms
from accounts.models import CustomUser
from core.models import Task
from core.mixins import BootstrapFormMixin

class CreateClientForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "name"]

class CreateTaskForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "client", "deadline", "file", ]        


