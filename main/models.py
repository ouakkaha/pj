from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_time = models.DateTimeField("data published")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title