from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
    path('create/', views.create_post, name='create'),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
    path('update/<slug:slug>/', views.UpdatePost.as_view(), name='update'),
]
