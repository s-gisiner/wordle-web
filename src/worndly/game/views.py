from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('game:home')
        
    return render(request, 'game/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password, name=name)
        return redirect('game:login')
    
    return render(request, 'game/signup.html')

def home(request):
    return render(request, 'game/home.html')