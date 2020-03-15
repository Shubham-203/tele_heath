from django.shortcuts import render,HttpResponse
from patientapp.models import Patient,PatientDiet,PatientAdmit,PatientAppoinmnt,PatientPrescription
# Create your views here.
from django.views import View
from patientapp.forms import PatientAppoinmntForm,PatientForm
from django.views.generic import *
from django.core.mail import send_mail

def sending_mail(request):
    send_mail('appointment confirmed',
    'your appointment is fixed, please be on time',
    'cjcdemo123@gmail.com',
    ['kushalkombe@gmail.com','swapnilsakhare93@gmail.com'])
    return render(request,'patientapp/email.html')

class PatientList(ListView):
    model = Patient
    def get_context_data(self, **kwargs): # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs) # Add in a QuerySet of all the books
        context['patient_list'] = Patient.objects.all().order_by('patient_name')
        return context
class PatientAppoinmnt(CreateView):
    model=PatientAppoinmnt
    fields='__all__'
    # print(patient_name,'****************')
    send_mail('Subject: Appointment Letter',
    "Dear [Applicant Name]"
    "Thank you for accepting and signing the job offer letter. I am pleased to inform you that your employment with us has been confirmed",
    'cjcdemo123@gmail.com',
    ['kushalkombe@gmail.com','m'],
    fail_silently=False)
    template_name='patientapp/appointment.html'
