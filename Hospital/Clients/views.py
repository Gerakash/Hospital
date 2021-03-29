from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import ClientSerializer, RegisterSerializer
from django.contrib.auth.models import User

from .tokens import account_activation_token


class ClientsView(views.APIView):

    def get(self,request,*args,**kwargs):
       clients = Client.objects.all()
       serializer = ClientSerializer(clients,many=True)
       return Response (serializer.data)




class RegisterConfirmView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html',{
                'user':user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = serializer.data['email']
            email = EmailMessage(subject=mail_subject,body=message,to=[to_email])
            email.send()
            return Response({"data":"Successfully"})
        return Response (serializer.errors)




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_staff = True
        user.save()
        login(request,user)
        return HttpResponse({"Okay!"})
    return HttpResponse({"Not Okay!"})






