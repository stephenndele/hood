
from django import forms

from .models import Hood



class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ('name', 'location', 'occupants', 'image')

        widgets = {
            'image': forms.TextInput(attrs={'placeholder': 'Add image url.... '}),
        }