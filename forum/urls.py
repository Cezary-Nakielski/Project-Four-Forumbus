from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
]
