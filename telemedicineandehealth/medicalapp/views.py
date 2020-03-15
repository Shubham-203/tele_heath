from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from medicalapp.models import Medical,Medicines,MedicalImage
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
