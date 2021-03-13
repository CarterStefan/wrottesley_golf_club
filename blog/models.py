from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):

    class Meta:
        ordering = ['-date_created']

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300, unique=True)
    main_image = models.ImageField()
    last_updated = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()

    def __str__(self):
        return self.title
