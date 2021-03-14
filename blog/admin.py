from django.contrib import admin
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'date_created',
    )

    search_fields = [
        'title',
        'content',
    ]

    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Blog, BlogAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'blog',
        'date_created',
        'approved'
    )

    list_filter = (
        'approved',
        'date_created'
    )

    search_fields = (
        'name',
        'body'
    )

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
