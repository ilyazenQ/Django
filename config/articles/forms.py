from django import forms
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'is_published', 'cat', 'tags']


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, **kwargs):
        self.clean()
        user = self.Meta.model(
            username = self.cleaned_data['username'],
            email = self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

