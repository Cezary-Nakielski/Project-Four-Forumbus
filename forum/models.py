from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    time = models.DateTimeField(auto_now=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-time"]

    def __str__(self):
        return self.title
