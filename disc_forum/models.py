from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.http.response import HttpResponseRedirect
from django.utils.timezone import now

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=1000000)

def __str__(self):
    return str(self.title)

class Comment(models.Model):
    post = models.ForeignKey(Forum, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField()
    repDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post.title) + " " + str(self.author)