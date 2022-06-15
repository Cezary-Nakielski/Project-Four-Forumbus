from django import forms
from forum.models import Post

# Post creation form model


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
