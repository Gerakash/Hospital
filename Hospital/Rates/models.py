from django.db import models
from Hospitals.models import Hospital, Doctor


# Create your models here.

class RateHospital(models.Model):
    star = models.PositiveIntegerField()
    hospitals = models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name='ratehospitals')



class RateDoctor(models.Model):
    star = models.PositiveIntegerField()
    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='ratedoctors')
