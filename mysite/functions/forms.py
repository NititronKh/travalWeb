from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'author', 'date', 'content', 'image', 'caption', 'youtube_url']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'ckeditor'}),  # ใช้ CKEditor
        }
