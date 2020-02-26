from django.conf import settings
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars  # or truncatewords


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_image', default=None, blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# function that limits the length of the string for admin interface
    @property
    def short_description(self):
        return truncatechars(self.text, 20)
