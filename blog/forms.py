from django import forms
from .widgets import CustomClearableFileInput
from .models import Blog, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('slug', 'title', 'main_image',
                  'sub_title_one', 'blog_content_one',
                  'sub_title_two', 'blog_content_two')

    main_image = (
        forms.ImageField(
            label="Main Image",
            required=True,
            widget=CustomClearableFileInput
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['slug'].widget.attrs['placeholder'] = (
            'e.g title-of-your-blog'
        )

        self.fields['title'].widget.attrs['placeholder'] = (
            'Title of your blog post'
        )

        self.fields['sub_title_one'].widget.attrs['placeholder'] = (
            'First subheading'
        )

        self.fields['blog_content_one'].widget.attrs['placeholder'] = (
            'First paragraph of your blog'
        )

        self.fields['sub_title_two'].widget.attrs['placeholder'] = (
            'Second subheading'
        )

        self.fields['blog_content_two'].widget.attrs['placeholder'] = (
            'Second paragraph of your blog'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

    body = forms.CharField(label="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['body'].widget.attrs['placeholder'] = 'Add a comment...'
