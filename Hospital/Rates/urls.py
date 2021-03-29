from django.urls import path

from .views import RateHospitalView, RateDoctorView

urlpatterns = [
    path('ratehospital/<int:hospital_id>/',RateHospitalView.as_view()),
    path('ratedoctor/<int:doctor_id>/',RateDoctorView.as_view())
]