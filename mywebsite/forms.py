from django import forms

from .models import Post, Comment, CreateWorkshop
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titleImage', 'title', 'text', 'ideaCategories', 'cofounderOfIdeas')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class CreateWorkshopForm(forms.ModelForm):
    class Meta:
        model = CreateWorkshop
        fields = ('WorkshopName', 'StartDate', 'EndDate', 'Subject', 'Topic', 'Venue', 'Description')
