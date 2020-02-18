from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image', 'title', 'text']


class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
