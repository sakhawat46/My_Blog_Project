from django import forms
from blog_app.models import Blog, Comment, Like

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)