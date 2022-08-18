from django.contrib import admin
from .models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time', 'approved')
    list_filter = ('approved', 'time')


admin.site.register(Profile)
