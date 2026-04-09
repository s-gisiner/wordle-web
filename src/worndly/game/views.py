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

def home(request):
    return render(request, 'game/home.html')