from rest_framework import serializers

from Rates.serializers import RateHospitalModelSerializer
from .models import *


class HospitalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ['categories','name','address','contact','email']


class DepartmentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Department
        fields = ['name']


class HospitalDetailSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    department_set = DepartmentSerializer(many=True)
    ratehospitals = RateHospitalModelSerializer(many=True)

    class Meta:
        model = Hospital
        fields = ['avg_rate','categories','name','address','contact','email','department_set','ratehospitals']


    def get_avg_rate(self, obj):
        total_star = 0
        for rate in obj.ratehospitals.all():
            total_star += rate.star
        return round(total_star / len(obj.ratehospitals.all()), 1)


class DoctorSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['avg_rate','occupation','image','full_name','education','department']


    def get_avg_rate(self, obj):
        total_star = 0
        for rate in obj.ratedoctors.all():
            total_star += rate.star
        return round(total_star / len(obj.ratedoctors.all()), 1)




class DepartmentDetailSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Department
        fields = ['name','doctors']





