
from django import forms
from django.contrib.auth.models import User
from .models import Hood, Profile, Post, Business
from django.contrib import messages




class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name', 'location', 'image', 'admin','health_tell', 'police_number' ) 

        widgets = {
            'image': forms.TextInput(attrs={'placeholder': 'Add image url.... '}),
        }


class ProfileUpdateForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('user', 'bio', 'profile_picture', 'location', 'hood')
 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ( 'title','post','user','hood')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('user','name', 'description','image','email','hood' )


    