from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def blog_list(request):
    """
    A view to return all the blog posts
    """
    all_blog_posts = Blog.objects.all().order_by('-date-created')

    context = {
        'all_blog_posts': all_blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    """ A view to show the individual blog post """
    blog_post = get_object_or_404(Blog, slug=slug)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'blog/blog_detail.html', context)
