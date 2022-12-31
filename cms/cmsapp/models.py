from cgitb import text
from email.policy import default
from django.db import models



class Members(models.Model):
  text = models.CharField(max_length=255)
  banner = models.ImageField(upload_to ="images/",default="")
  about=models.CharField(max_length=255)
class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  subject = models.CharField(max_length=255)
class Reviews(models.Model):
  user = models.CharField(max_length=255)
  image = models.ImageField(upload_to ="images/",default="")
  feed = models.CharField(max_length=25)

