from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Class based view for displaying list of posts


class PostsList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('-time')
    template_name = 'index.html'
    paginate_by = 7

# Class based view for displaying content of a selected post


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

# Function based view for creating a post


@login_required
def create_post(request):
    post_form = PostForm()
    print(request.method)
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        print(post_form.is_valid())
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.title = post_form.title.title()
            post_form.creator = request.user
            post_form.save()
            messages.success(request, 'The post had been successfully created')
            return redirect('homepage')

    return render(request, 'create.html', context={'post_form':
                  post_form})

# Class based view for updating a post


class UpdatePost(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    template_name = 'post_update_form.html'
    success_url = '/'
    success_message = "The post had been successfully updated"

# Class based view for updating a post


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'
