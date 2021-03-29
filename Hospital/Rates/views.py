from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response
from Hospitals.models import Hospital, Doctor
from Rates.models import RateHospital, RateDoctor
from Rates.serializers import RateHospitalSerializer, RateDoctorSerializer


class RateHospitalView(views.APIView):

    def post(self,request,*args,**kwargs):
        hospital = Hospital.objects.get(id=kwargs['hospital_id'])
        serializer = RateHospitalSerializer(data=request.data)
        if serializer.is_valid():
            star = serializer.data.get('star')
            RateHospital.objects.create(hospitals=hospital,star=star)
            return Response({"data":"thank you for rating!"})
        return Response(serializer.errors)



class RateDoctorView(views.APIView):

    def post(self,request,*args,**kwargs):
        doctor = Doctor.objects.get(id=kwargs['doctor_id'])
        serializer = RateDoctorSerializer(data=request.data)
        if serializer.is_valid():
            star = serializer.data.get('star')
            RateDoctor.objects.create(doctors=doctor,star=star)
            return Response({"data":"thank you for rating!"})
        return Response(serializer.errors)




