from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    extra_plays = models.IntegerField(default=0)

    def __str__(self):
        return self.username