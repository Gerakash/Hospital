from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Hospital(models.Model):
    categories = (
        ('goverment', 'goverment'),
        ('private', 'private')
    )
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,blank=False)
    contact = models.IntegerField(default=0)
    email = models.CharField(max_length=100,blank=True)



class Department(models.Model):
    name = models.CharField(max_length=100)
    hospitals = models.ForeignKey('Hospital',on_delete=models.CASCADE,blank=False)

    def __str__(self):
        try:
            return f"Hospital: {self.hospitals.name}, dep: {self.name}"
        except AttributeError:
            return self.name



class Doctor(models.Model):
    occupation = models.CharField(max_length=100)
    image = models.ImageField()
    full_name = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=False, related_name='doctors')









