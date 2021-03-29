from django.shortcuts import render

# Create your views here.
from rest_framework import views, status
from rest_framework.response import Response

from Comments.models import Comment
from Comments.serializers import DoctorDetailSerializer, CommentCreateSerializer
from Hospitals.models import Doctor


class DoctorDetailView(views.APIView):

    def get(self, request, *args, **kwargs):
        try:
            book = Doctor.objects.get(id=kwargs['doctor_id'])
        except Doctor.DoesNotExist:
            return Response({"data": "NotFound"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorDetailSerializer(book)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            doctor = Doctor.objects.get(id=kwargs['doctor_id'])
            text = serializer.data.get('text')
            Comment.objects.create(doctor=doctor, text=text, user=request.user)
            return Response({"data": "comment create succesfully!"})
        return Response(serializer.errors)


