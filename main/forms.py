
from django import forms
from django.contrib.auth.models import User
from .models import Hood, Profile



class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name', 'location', 'occupants', 'image')

        widgets = {
            'image': forms.TextInput(attrs={'placeholder': 'Add image url.... '}),
        }


class ProfileForm(forms.ModelForm):
	class Meta: 
		model = Profile
		fields = ('user', 'bio', 'profile_picture', 'location', 'hood')
 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
