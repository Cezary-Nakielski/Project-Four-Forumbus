from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
]
