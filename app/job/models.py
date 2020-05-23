from django.db import models

class Job(models.Model):
    profile = models.CharField(max_length=256)
    client = models.CharField(max_length=64)
    requirements = models.CharField(max_length=256)

# Create your models here.
