from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostsList.as_view(), name="homepage"),
]