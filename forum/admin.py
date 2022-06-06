from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time', 'approved')
    list_filter = ('approved', 'time')
    search_fields = ('title', 'body', 'creator')
    action = ['approve_comments']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)
