from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='threads')
    time = models.DateTimeField(default=timezone.now)
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=800)

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments')
    time = models.DateTimeField(default=timezone.now)
    content = models.TextField(max_length=800)

