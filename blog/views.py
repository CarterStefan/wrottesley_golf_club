from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogPostForm, CommentForm

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


def add_blog(request):
    """ A view to add a new blog post """
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New blog post uploaded')
            return redirect(reverse('add_blog'))
        else:
            messages.error(request, 'There was an error. Please try again')
    else:
        form = BlogPostForm()

    context = {
        'form': form
    }

    return render(request, 'blog/add_new_blog.html', context)


def edit_blog(request, slug):
    """ A view to edit a blog post """
    blog_post = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{blog_post.title} updated')
            return redirect(reverse('blog_detail', args=[blog_post.slug]))
        else:
            messages.error(request, 'There was an error. Please try again')
    else:
        form = BlogPostForm(instance=blog_post)
        messages.info(request, f'Now editing {blog_post.title}')

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, 'blog/edit_blog.html', context)
