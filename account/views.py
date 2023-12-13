from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def RegisterPage(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            first_name=request.POST['first_name'],
            password=request.POST['password']
        )
        return redirect('home')
    return render(request, 'account/register.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'account/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

