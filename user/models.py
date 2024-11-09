from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    TYPE_OF_USER = [
        ('Hiring', 'Hiring'),
        ('Service', 'Service'),
        ('User', 'User'),
    ]

    email = models.EmailField(unique=True)
    type = models.CharField(max_length=7, choices=TYPE_OF_USER, default='User')
