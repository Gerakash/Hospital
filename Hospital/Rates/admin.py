from django.contrib import admin

# Register your models here.
from Rates.models import RateHospital, RateDoctor

admin.site.register([RateHospital,RateDoctor])