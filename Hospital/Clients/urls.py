from django.urls import path
from rest_framework import views

from .views import ClientsView,RegisterConfirmView,activate

urlpatterns = [
    path ('client/',ClientsView.as_view()),
    path ('register/',RegisterConfirmView.as_view()),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate')
]