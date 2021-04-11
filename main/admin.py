from django.contrib import admin
from .models import Hood, Business, Post, Profile

# Register your models here.
admin.site.register(Hood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Profile)