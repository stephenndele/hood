from . import views
from django.urls import path


app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('addhood', views.add_hood, name='add_hood'),
    path("user/", views.userpage, name = "userpage"),
    path('<hood_id>/new-post', views.create_post, name='post'),
    path('details/<int:id>', views.details, name='details'),
    path('<hood_id>/new-business', views.create_business, name='business'),
    path('edithoods/<int:id>/', views.edit_hoods, name='edit_hoods'),
    path('deletehoods/<int:id>/', views.delete_hoods, name='delete_hoods'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('api/hood/', views.HoodList.as_view()),
    path('api/view_hood/', views.ViewHoodList.as_view()),
    path('search/', views.search_business, name='search'),

]