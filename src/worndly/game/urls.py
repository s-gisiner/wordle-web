from django.urls import path

from . import views
app_name = 'game'  # creates a namespace for this app
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
]
