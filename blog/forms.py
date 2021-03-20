from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('slug', 'title', 'main_image',
                  'sub_title_one', 'blog_content_one',
                  'sub_title_two', 'blog_content_two')

    main_image = forms.ImageField(label="Main Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['blog_content_one'].widget.attrs['placeholder'] = 'Blog content_one'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
