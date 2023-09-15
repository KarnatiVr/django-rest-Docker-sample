from django.db import models

# Create your models here.

# Create your models here.
class myDetails(models.Model):
    name= models.CharField(max_length=80)
    email= models.CharField(max_length=80)
    phno = models.CharField(max_length=80)
    college= models.CharField(max_length=100)
    skills= models.CharField(max_length=500)
    