from django.db import models

# Create your models here.

class Turfs(models.Model):

    title = models.CharField(max_length=200)
    #date = models.DateField()
    #time= models.CharField(max_length=200)
    booked = models.IntegerField(default=1)
   
class User(models.Model):
    pass