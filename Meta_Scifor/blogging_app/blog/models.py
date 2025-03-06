from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})