from . import views
from django.urls import path
from forum.views import PostCreate

urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
    path('create/', PostCreate.as_view(), name='create'),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
]
