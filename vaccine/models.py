from django.db import models

# Create your models here.
class Vaccine(models.Model) :
    vaccine_name = models.CharField(max_length=30)
    ingredient = models.TextField()
    minimum_age = models.CharField(max_length=50)
    doses_gap = models.TextField()