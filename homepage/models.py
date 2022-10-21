from django.db import models
from django.db.models.base import Model

# Create your models here.
class Feedback(models.Model):
    username = models.CharField(max_length=30)
    feedback = models.TextField()