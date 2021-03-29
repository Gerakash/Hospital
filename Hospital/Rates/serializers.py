from rest_framework import serializers

from Rates.models import RateHospital, RateDoctor


class RateHospitalSerializer(serializers.Serializer):
    star = serializers.IntegerField(max_value=10,min_value=0)

class RateHospitalModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateHospital
        fields = ['star','hospitals']



class RateDoctorSerializer(serializers.Serializer):
    star = serializers.IntegerField(max_value=10,min_value=0)


class RateDoctorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateDoctor
        fields = ['star','doctors']