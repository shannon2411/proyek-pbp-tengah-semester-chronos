from django.db import models

# Create your models here.
class Apotik(models.Model):
    daerah = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
