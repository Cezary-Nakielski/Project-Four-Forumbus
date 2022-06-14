from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Class based view for displaying list of posts


class PostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-time')
    template_name = 'index.html'
    paginate_by = 9

# Class based view for displaying content of posts


class PostContent(View):

    def get(self, request, slug):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_content.html",
            {
                "post": post,
            },
        )
