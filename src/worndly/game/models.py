from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
class Play(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='plays'
    )

    word_guessed = models.CharField(max_length=5)
    is_win = models.BooleanField(default=False)
    attempts = models.IntegerField()

    date_played = models.DateTimeField(auto_now_add=True)