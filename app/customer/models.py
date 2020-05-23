from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

# Create your models here.
