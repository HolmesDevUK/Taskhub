from django import forms
from accounts.models import CustomUser
from core.models import Task

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "name"]

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "client", "deadline", "file", ]        


