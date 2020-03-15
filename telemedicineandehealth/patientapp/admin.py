from django.contrib import admin
from patientapp.models import Patient,PatientAppoinmnt

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display=['id','patient_registration_number','patient_name','patient_contact','patient_address','patient_symptoms']
admin.site.register(Patient,PatientAdmin)
admin.site.register(PatientAppoinmnt)
