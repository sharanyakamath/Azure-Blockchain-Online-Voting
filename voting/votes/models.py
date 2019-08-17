
# Create your models here.
#import webcam.admin 
# needed to show the right widget in the admin
from django.db import models
#from webcam.fields import CameraField

class Person(models.Model):
	username = models.CharField(max_length=255, primary_key=True, default="abc")
	picture = models.ImageField()