from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
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

# Function based view for creating post


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
            return redirect('homepage')

    return render(request, 'create.html', context={'post_form':
                  post_form})

# Class based view for Updating a post


class UpdatePost(UpdateView):
    model = Post()
    form_class = PostForm
    template_name_suffix = '_update_form'
    template_name = 'update.html'
    success_url = '/'
