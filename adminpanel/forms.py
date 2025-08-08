from django import forms
from accounts.models import CustomUser

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "name"]


