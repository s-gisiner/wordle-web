from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
app_name = 'game'  # creates a namespace for this app
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(next_page='game:login'), name='logout'),
]
