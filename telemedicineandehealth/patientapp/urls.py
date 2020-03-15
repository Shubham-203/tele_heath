from django.urls import path
from patientapp import views
urlpatterns = [
    path('email/',views.sending_mail),
    path('patilist/',views.PatientList.as_view()),
    path('appoint/',views.PatientAppoinmnt.as_view()),
    ]
