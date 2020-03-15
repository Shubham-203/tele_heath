from django.shortcuts import render,HttpResponse,redirect
from hospitalapp.models import DoctorSpeciality,Hospital,HospitalDoctor,HospitalImages
# Create your views here.
from hospitalapp.models import Hospital
from django.views.generic import *
from django.views import View
from hospitalapp.forms import HospitalForm
from passlib.hash import pbkdf2_sha256

class HospitalView(ListView):
    model = Hospital
    template_name = 'hospitalapp/hospital_list.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(HospitalView, self).get_queryset()
       query = self.request.GET.get('search')
       result = Hospital.objects.all()
       # if query:
       #    postresult = Hospital.objects.filter(hospital_name__contains=query)
       #    result = postresult
       # else:
       #     result = Hospital.objects.all()
       return result
class HospitalDetail(DetailView):
    model=Hospital
    template_name = 'hospitalapp/hospital_detail.html'

class HospitalCreate(View):
    def get(self,request):
        form=HospitalForm()
        return render(request,'hospitalapp/hospital_create.html',{'form':form})
    def post(self,request):
        form=HospitalForm(request.POST)
        hospital_name=request.POST.get('hospital_name')
        hospital_address=request.POST.get('hospital_address')
        hospital_info=request.POST.get('hospital_info')
        hospital_type=request.POST.get('hospital_type')
        goverment_scheme=request.POST.get('goverment_scheme')
        hospital_contact=request.POST.get('hospital_contact')
        hospital_speciality=request.POST.get('hospital_speciality')
        membership_available=request.POST.get('membership_available')
        blood_bank=request.POST.get('blood_bank')
        hospital_lab=request.POST.get('hospital_lab')
        hospital_ambulance=request.POST.get('hospital_ambulance')
        hospital_bed=request.POST.get('hospital_bed')
        hospital_icu=request.POST.get('hospital_icu')
        hospital_email=request.POST.get('hospital_email')
        hospital_password=request.POST.get('hospital_password')
        encrypt_password=pbkdf2_sha256.encrypt(hospital_password,rounds=12000,salt_size=32)
        if form.is_valid():
            print('*******************')
            Hospital.objects.create(hospital_name=hospital_name,hospital_address=hospital_address,hospital_info=hospital_info,hospital_type=hospital_type,goverment_scheme=goverment_scheme,
            hospital_contact=hospital_contact,hospital_speciality=hospital_speciality,membership_available=membership_available,blood_bank=blood_bank,hospital_lab=hospital_lab,
            hospital_ambulance=hospital_ambulance,hospital_bed=hospital_bed,hospital_icu=hospital_icu,hospital_email=hospital_email,hospital_password=encrypt_password)
            return redirect('/admin/')
        return render(request,'hospitalapp/hospital_create.html',{'form':form})
