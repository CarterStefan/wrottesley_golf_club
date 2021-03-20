from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):

    class Meta:
        ordering = ['-date_created']

    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(null=False, blank=False)
    title = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    sub_title_one = models.CharField(max_length=300, unique=True, null=False, blank=False,)
    blog_content_one = models.TextField(null=False, blank=False,)
    sub_title_two = models.CharField(max_length=300, null=True, blank=True,)
    blog_content_two = models.TextField(null=True, blank=True,)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog_detail", kwargs={"slug": str(self.slug)})


class Comment(models.Model):

    class Meta:
        ordering = ['-date_created']

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
