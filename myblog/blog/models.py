from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Add the custom manager which retrieve all posts that have a PUBLISHED status
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    # status class to save posts as a draft until ready for publication
    DoesNotExist = None

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    # We will use the slug field to build beautiful, SEO-friendly URLs for blog posts
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_post')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,  # enumeration type
                              default=Status.DRAFT)

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager

    class Meta:
        ordering = ['-publish']
        indexes = [
            # More information about how to define indexes for models
            # https://docs.djangoproject.com/en/4.1/ref/models/indexes/
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
