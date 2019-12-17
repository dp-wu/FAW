"""
Notes:
    1. Question about timezone.now and timezone.now():
        If you remove the parentheses (in this case,
        try default=timezone.now) then you're passing a callable to the
        model and it will be called each time a new instance is saved. With
        the parentheses, it's only being called once when models.py loads.
        -- Answered by Jamey Sharp on stackoverflow
"""

from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    """
    1. define Post object.
    2. models.Model: the Post is a Django Model, so Django knows
        that it should be saved in the database.
    3. there are other model fields, we can find them in the django
        official document.
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

