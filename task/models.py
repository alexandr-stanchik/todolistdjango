from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_start = models.DateTimeField()
    is_done = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
