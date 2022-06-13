from . import views
from django.urls import path
from views import PostCreate

urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
    path('create/', PostCreate.as_view(), name='create'),
]
