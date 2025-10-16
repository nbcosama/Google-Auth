# accounts/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    name = request.user.get_full_name() if request.user.is_authenticated else 'Guest'
    email = request.user.email if request.user.is_authenticated else 'Not logged in'
    print(f"User Name: {name}, Email: {email}")
    return render(request, 'home.html')
