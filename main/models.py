from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=1000)
    occupants = models.CharField(max_length=500)
    image = models.URLField(
        default='default.jpg')
    # admin = models.ForeignKey('Admin', on_delete=models.CASCADE)