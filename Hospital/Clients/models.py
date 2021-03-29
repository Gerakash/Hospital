from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Client(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)
    phone_number = models.PositiveIntegerField(default=0,blank=True)
    email = models.CharField(max_length=100,blank=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
