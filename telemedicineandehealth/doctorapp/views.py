from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from doctorapp.forms import DoctorForm
from django.views import View
from passlib.hash import pbkdf2_sha256
from doctorapp.models import Doctor
# Create your views here.
class FrontView(TemplateView):
    template_name = "doctorapp/index.html"

class DoctorCreate(View):
    def get(self,request):
        form=DoctorForm()
        return render(request,'doctorapp/doctor_create.html',{'form':form})
    def post(self,request):
        form=DoctorForm(request.POST)
        doctor_name=request.POST.get('doctor_name')
        doctor_qualification=request.POST.get('doctor_qualification')
        doctor_experience=request.POST.get('doctor_experience')
        doctor_gender=request.POST.get('doctor_gender')
        doctor_speciality=request.POST.get('doctor_speciality')
        doctor_contact=request.POST.get('doctor_contact')
        # doctor_image=request.POST.get('doctor_image')
        doctor_info=request.POST.get('doctor_info')
        doctor_email=request.POST.get('doctor_email')
        doctor_password=request.POST.get('doctor_password')
        encrypt_password=pbkdf2_sha256.encrypt(doctor_password,rounds=12000,salt_size=32)
        if form.is_valid():
            Doctor.objects.create(doctor_name=doctor_name,doctor_qualification=doctor_qualification,doctor_experience=doctor_experience,
            doctor_gender=doctor_gender,doctor_speciality=doctor_speciality,doctor_contact=doctor_contact,
            doctor_info=doctor_info,doctor_email=doctor_email,doctor_password=encrypt_password)
            return redirect('/admin/')
        return render(request,'doctorapp/doctor_create.html',{'form':form})
