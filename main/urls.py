from .views import home
from django.urls import path




urlpatterns = [
    path('', views.home, name='home'),

]