from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# pylint: disable=too-few-public-methods
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    class Meta:
        ordering = ("-publish",)

    # The default manager
    objects = models.Manager()

    # Our custom manager. Use it by calling `Post.published.???`
    published = PublishedManager()

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.title  # pylint: disable=invalid-str-returned

    def get_absolute_url(self):
        """Builds a custom url for this model."""
        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )
