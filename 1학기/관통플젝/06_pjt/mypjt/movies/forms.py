from django import forms
from .models import Movie, Comment



class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('user_id', 'user_liked',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie_id', 'user_id',)