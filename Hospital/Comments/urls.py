from django.urls import path

from Comments.views import DoctorDetailView

urlpatterns = [
    path('comments/<int:doctor_id>/',DoctorDetailView.as_view()),
]