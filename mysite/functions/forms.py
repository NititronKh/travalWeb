from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'author', 'date', 'content', 'image', 'image1', 'image2', 'caption', 'youtube_url', 'type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
