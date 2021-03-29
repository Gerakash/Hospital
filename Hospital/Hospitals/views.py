from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.response import Response

from .models import *
from .serializers import *


class HospitalsView(views.APIView):

    def get(self, request, *args, **kwargs):
        hospital = Hospital.objects.all()
        serializer = HospitalSerializer(hospital,many=True)
        return Response(serializer.data)


class DepartmentsView(views.APIView):

    def get(self,request, *args,**kwargs):
        hospitals = Hospital.objects.get(id=kwargs['hospital_id'])
        serializer = HospitalDetailSerializer(hospitals)
        return Response(serializer.data)


class DoctorsView(views.APIView):

    def get(self,request,*args,**kwargs):
        departments = Department.objects.get(id=kwargs['department_id'])
        serializer = DepartmentDetailSerializer(departments)
        return Response(serializer.data)



