from . import views
from django.urls import path


app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('addhood', views.add_hood, name='add_hood'),

]