from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('slug','title', 'main_image', 'blog_content')

    main_image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['blog_content'].widget.attrs['placeholder'] = 'Blog content'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
