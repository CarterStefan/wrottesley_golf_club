from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Blog
from .forms import CommentForm

# Create your views here.


def blog_list(request):
    """
    A view to return all the blog posts
    """
    all_blog_posts = Blog.objects.all().order_by('-date_created')

    context = {
        'all_blog_posts': all_blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    """ A view to show the individual blog post """
    blog_post = get_object_or_404(Blog, slug=slug)
    comments = blog_post.comments.filter(approved=True).order_by("-date_created")
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog = blog_post
            messages.success(request, 'Thank you for your comment, it has been sent for approval and will appear once done')
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_detail.html', context)
