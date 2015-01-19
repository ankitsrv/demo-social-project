from django import forms
from newsfeed.models import Post, Like

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        exclude = ['comment']



class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('sender', 'no_of_likes')