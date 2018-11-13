from django.db import models
from django.utils import timezone

class Task(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)

  created_at = timezone.now
  updated_at = timezone.now
