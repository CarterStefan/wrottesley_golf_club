from django import forms
from .models import Blog, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs['auto-focus'] = True
        self.fields['title'].widget.attrs['placeholder'] = 'Blog post title'
        self.fields['blog_content'].widget.attrs['placeholder'] = 'Blog content'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
