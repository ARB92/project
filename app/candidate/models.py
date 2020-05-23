from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    qualification = models.CharField(max_length=32)
    skills = models.CharField(max_length=256)
    experience = models.CharField(max_length=2)
    resume = models.FileField(upload_to ='resume')

# Create your models here.
