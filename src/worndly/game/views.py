from django.shortcuts import render
from .models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username, password=password).first()
        if user:
            return render(request, 'game/home.html')
        
    return render(request, 'game/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(name=name, username=username, email=email, password=password)
        return render(request, 'game/login.html')
    
    return render(request, 'game/signup.html')

def home(request):
    return render(request, 'game/home.html')