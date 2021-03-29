from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Hospitals.models import Doctor


class Comment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


