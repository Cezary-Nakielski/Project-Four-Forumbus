from django.shortcuts import render
from django.views import generic
from .models import Post


class PostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-time')
    template_name = 'index.html'
    paginate_by = 9

# Create your views here.
