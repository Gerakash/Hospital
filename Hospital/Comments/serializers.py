from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Comment


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(Serializer):
    text = CharField(allow_blank=False)
    pass



