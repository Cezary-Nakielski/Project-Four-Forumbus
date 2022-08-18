from django.contrib import admin
from .models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'time', 'approved')
    list_filter = ('approved', 'time')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'location')
    list_filter = ('age', 'location')
    search_fields = ('username', 'first_name', 'surname', 'email', 'location')
