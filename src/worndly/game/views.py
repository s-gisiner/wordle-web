from django.utils import timezone
from datetime import timedelta

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

from .kratos_api import view_balance_for_user
from .models import User
from .models import User, Play
from django.conf import settings
import json

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('game:home')
        else:
            # Check if user exists with plain text password
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    user.password = make_password(password)
                    user.save()
                    auth_login(request, user)
                    return redirect('game:home')
            except User.DoesNotExist:
                pass
        
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

@login_required
def home(request):
    return render(request, 'game/home.html')

def logout_view(request):
    auth_logout(request)
    return redirect('game:login')

@login_required
def play(request):
    return render(request, 'game/play.html')

@login_required
def profile(request):
    plays = Play.objects.order_by('-date_played')
    plays = plays.filter(user=request.user)
    try:
        filter_type = request.GET.get('filter')
    except:
        filter_type = "all"
    curr_time = timezone.now()

    if filter_type == 'week':
        start_date = curr_time - timedelta(days=7)
        plays = plays.filter(date_played__gte=start_date)
        
    elif filter_type == 'month':
        start_date = curr_time - timedelta(days=30)
        plays = plays.filter(date_played__gte=start_date)
        
    elif filter_type == 'year':
        start_date = curr_time - timedelta(days=365)
        plays = plays.filter(date_played__gte=start_date)

    context = {
        'plays': plays,
    }
    return render(request, 'game/profile.html', context)

@login_required
def buy_games(request):
    user = request.user
    balance_response = view_balance_for_user(settings.KRATOS_ACCESS_TOKEN, user.email)

    if balance_response:
        balance = balance_response.get('amount', 0)
    else:
        balance = None

    return render(request, 'game/buy_games.html', {"balance": balance, "extra_plays": user.extra_plays})
    

def save_game_result(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            Play.objects.create(
                user=request.user,
                word_guessed=data.get('word'),
                is_win=data.get('is_win'),
                attempts=data.get('attempts'),
            )
            
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'invalid method'}, status=405)
