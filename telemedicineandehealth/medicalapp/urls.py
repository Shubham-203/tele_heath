from django.urls import path
from medicalapp import views
urlpatterns = [
    path('list/',views.MedicalView.as_view()),
    path('create/',views.MedicalCreate.as_view()),
    path('list/<int:pk>/',views.MedicalDetail.as_view(),name='detail'),
    # path('list/',views.hospital_overview)
    ]
