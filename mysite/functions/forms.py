# functions/forms.py
from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'author', 'date', 'content', 'image', 'caption','youtube_url']
        help_texts = {
            'title': 'ไมจำเป็นต้องกรอก',
            'author': 'ไมจำเป็นต้องกรอก',
            'date': 'ไมจำเป็นต้องกรอก',
            'content': 'ไมจำเป็นต้องกรอก',
            'image': 'ไมจำเป็นต้องกรอก',
            'caption': 'ไมจำเป็นต้องกรอก',
            'youtube_url': 'เปลี่ยนลิงก์เป็น embed/ แทน wacth?v= เช่น https://www.youtube.com/watch?v=VIDEO_ID เป็น https://www.youtube.com/embed/VIDEO_ID',
        }
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))