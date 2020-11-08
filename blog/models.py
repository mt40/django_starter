from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# pylint: disable=too-few-public-methods
from taggit.managers import TaggableManager


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

    # a manager from 3rd party library to manage tags
    tags = TaggableManager()

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

    # pylint: disable=invalid-str-returned
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Builds a custom url for this model."""
        return reverse(
            "blog:post_detail",
            # pylint: disable=no-member
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )


class Comment(models.Model):
    # set a custom related name so we can refer to all comments of the linked
    # Post by calling `post_instance.comments`
    #
    # See:
    #  https://docs.djangoproject.com/en/3.1/topics/db/queries/#backwards-related-objects
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # to deal with inappropriate comments
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return "Comment by {} on {}".format(self.name, self.post)
