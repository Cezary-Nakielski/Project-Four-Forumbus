from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView, UpdateView, DeleteView

# Class based view for displaying list of posts


class PostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-time')
    template_name = 'index.html'
    paginate_by = 9

# Class based view for displaying content of posts


class PostContent(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_content.html",
            {
                "post": post,
            },
        )


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = '/'
