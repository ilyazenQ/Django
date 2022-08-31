from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'is_published', 'cat','tags']