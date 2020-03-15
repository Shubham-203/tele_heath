from django.urls import path
from doctorapp import views
urlpatterns = [
    # path('list/',views.HospitalView.as_view()),
    path('create/',views.DoctorCreate.as_view()),
    # path('list/<int:pk>/',views.HospitalDetail.as_view(),name='detail'),
    # path('list/',views.hospital_overview)
    ]
