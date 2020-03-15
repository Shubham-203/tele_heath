from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from medicalapp.models import Medical,Medicines,MedicalImage
from medicalapp.forms import MedicalForm
from passlib.hash import pbkdf2_sha256
from django.views import View
# Create your views here.

from django.views.generic import *

class MedicalView(ListView):
    model = Medical
    template_name = 'medicalapp/medical_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(MedicalView, self).get_queryset()
       query = self.request.GET.get('search')
       result = Medical.objects.all()
       # if query:
       #    postresult = Hospital.objects.filter(hospital_name__contains=query)
       #    result = postresult
       # else:
       #     result = Hospital.objects.all()
       return result

class MedicalDetail(DetailView):
    model=Medical
    template_name = 'medicalapp/medical_detail.html'


class MedicalCreate(View):
    def get(self,request):
        form=MedicalForm()
        return render(request,'medicalapp/medical_create.html',{'form':form})
    def post(self,request):
        form=MedicalForm(request.POST)
        medical_name=request.POST.get('medical_name')
        medical_address=request.POST.get('medical_address')
        online_delivery=request.POST.get('online_delivery')
        medical_contact=request.POST.get('medical_contact')
        medical_email=request.POST.get('medical_email')
        medical_password=request.POST.get('medical_password')
        encrypt_password=pbkdf2_sha256.encrypt(medical_password,rounds=12000,salt_size=32)
        
        if form.is_valid():
            Medical.objects.create(medical_name=medical_name,medical_address=medical_address,
            online_delivery=online_delivery,medical_contact=medical_contact,medical_email=medical_email,medical_password=encrypt_password)
            return redirect('/admin/')
        return render(request,'medicalapp/medical_create.html',{'form':form})
