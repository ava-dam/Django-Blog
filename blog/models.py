from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# importing user model
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # auto_now=True is good for last modified, not for our case
    # auto_now_add=True cannot let you update the date, but puts date
    # of modification
    # models.CASCADE deletes post if user is deleted

    def __str__(self):
        return self.title

    # find url to any specific post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
