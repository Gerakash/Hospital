from django.urls import path
from .views import *

urlpatterns = [
    path('',HospitalsView.as_view()),
    path('department/<int:hospital_id>/',DepartmentsView.as_view()),
    path('doctor/<int:department_id>/',DoctorsView.as_view()),
]