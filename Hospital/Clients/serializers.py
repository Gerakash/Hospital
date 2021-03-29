from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['full_name','age','phone_number','email','user']


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields = ['username','email','password','confirm_password']


    def create(self,validated_data):
        password = validated_data.pop('password')
        if password != validated_data.pop('confirm_password'):
            raise ValidationError("not ok!")
        user = User(username=validated_data.pop('username'),email=validated_data.pop('email'))
        user.set_password(password)
        user.save()
        return user

