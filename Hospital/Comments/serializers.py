from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from Hospitals.models import Doctor
from Hospitals.serializers import DoctorSerializer
from .models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(Serializer):
    text = CharField(allow_blank=False)




class DoctorDetailSerializer(ModelSerializer):
    comment_set = CommentSerializer(many=True)


    class Meta:
        model = Doctor
        fields = '__all__'








