from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    """Displays a splash page"""
    return render(request, "programmer/index.html")

def register(request):
    """User registration."""
    #if request.method == "GET"
    return render(request, "programmer/register.html")

def login_view(request):
    """Log user in."""
    return render(request, "programmer/login.html")

def logout_view(request):
    """Log user out."""
    logout(request)
    context = {
        "alert_msg": "Succesfully logged out!"
    }
    return render(request, "programmer/login.html", context)
