from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    user = request.user

    if user.role == 'admin':
        return redirect('adminpanel:dashboard')
    elif user.role == 'client':
        return redirect('client:dashboard')
    else:
        return redirect('login')